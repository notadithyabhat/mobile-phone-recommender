from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
from sklearn.preprocessing import normalize
import pickle
import os

class Recommender():
	def __init__(self):
		self.X_mean=[4.72058824e+04,2.67058824e+00,2.47058824e+00,2.54705882e+00,2.40588235e+00,2.55882353e+00],
		self.X_std= [3.59828631e+04, 1.67604742e+00, 1.67745069e+00, 1.73565300e+00,1.76734117e+00, 1.71483452e+00]
		self.y_mean=[3.91636524e+05, 7.37647059e+00, 1.05717647e+02, 8.62235294e+01, 1.10010000e+03, 4.42355882e+03]
		self.y_std= [1.85555986e+05, 3.35358095e+00, 1.88190215e+01, 1.72578211e+01, 2.26216441e+02, 7.96081462e+02]
		self.results = []

	def recommend(self,data):
		X_pred = []
		recommender = load_model("Model.h5")
		for val in list(data.values())[:-2]:
			try:
				x = int(val)
			except:
				x=val
			X_pred.append(x)
		print(X_pred)
		os=X_pred.pop(1)
		X_pred = np.array(X_pred)
		budget = X_pred[0]
		X_pred = (X_pred - self.X_mean)//self.X_std
		newX = X_pred
		print(newX.shape)
		y_pred = recommender.predict(newX)
		ans = y_pred[0]
		for i in range(len(ans)):
			ans[i] = ans[i]*self.y_std[i] + self.y_mean[i]
			ans[i] = int(ans[i])
		pred =np.array([ans])
		self.results.append({'pro':ans[0],'ram':ans[1],'bc':ans[2],'fc':ans[3],'res':ans[4],'btr':ans[5]})

		db = pd.read_excel("Mobile Dataset.xlsx")

		mobiles=db.iloc[:,:2].to_numpy()
		specs=db.iloc[:,[3,4,5,7,8,9]].to_numpy()

		choices = {}
		MAXSIZE = 5
		pred = normalize(pred)
		specs = normalize(specs)
		for i in range(len(specs)):
		    diff = 0
		    for j in range(len(specs[0])):
		        diff+=abs((specs[i][j]-pred[0][j]))
		    if db["Price"][i]<=budget and db["OS"][i]==os:
		        choices[i]=diff

		choices=dict(sorted(choices.items(), key=lambda item: item[1]))


		try:
			with open("priority.pkl",'rb') as f:
				priority,lr = pickle.load(f)
		except:
			priority = {}
			lr=0.34

		search = ",".join([str(each) for each in X_pred])
		if search not in priority:
			priority[search] = [5,4,3,2,1]
			lr=0.34

		show_list = list(choices.keys())[:MAXSIZE]

		for i in range(len(priority[search])-1):
			for j in range(i+1,len(priority[search])):
				if priority[search][i]<priority[search][j]:
					priority[search][i],priority[search][j]=priority[search][j],priority[search][i]
					show_list[i],show_list[j]=show_list[j],show_list[i]

		for i,mobile in enumerate(show_list):
			m_processor, m_ram, m_bcam, m_fcam, m_screen, m_battery = db["Processor"][mobile], db["Ram"][mobile], db["Back Camera"][mobile], db["Front Camera"][mobile], db["Screen"][mobile], db["Battery"][mobile]
			self.results.append({"Mobile":f"{mobiles[mobile][0]} {mobiles[mobile][1]}",'pro':m_processor,'ram':m_ram,'bc':m_bcam,'fc':m_fcam,'res':m_screen,'btr':m_battery,'link':f'https://www.amazon.in/s?k={mobiles[mobile][0]}+{"+".join(mobiles[mobile][1].split(" "))}+8&ref=nb_sb_noss_2','idx':i+1})

		'''choice=int(input("Your choice? (1/2/3/4/5)"))
		print(priority[search])
		priority[search][choice-1]+=self.lr'''
		with open("priority.pkl",'wb') as f:
			pickle.dump([priority,lr],f,pickle.HIGHEST_PROTOCOL)
		return self.results,search


def update(choice,search):
	lr = int(choice)
	with open("priority.pkl",'rb') as f:
				priority,lr = pickle.load(f)
	print("Search is:",search)
	print("LR is:",lr)
	priority[search][choice-1]+=lr
	with open("priority.pkl",'wb') as f:
			pickle.dump([priority,lr],f,pickle.HIGHEST_PROTOCOL)



