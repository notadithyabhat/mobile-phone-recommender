import os
os.environ['PYTHONHASHSEED']=str(1)

import random
import pandas as pd
import numpy as np
from numpy import mean, std, asarray
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, normalize
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.model_selection import RepeatedKFold

 
def get_dataset():
	dataset = pd.read_excel("Final Mobile Dataset 2.xlsx")
	X = dataset.iloc[:,1:7]
	y = dataset.iloc[:,7:]
	X=X.to_numpy()
	y=y.to_numpy()
	return X,y


def get_model(n_inputs, n_outputs):
	model = Sequential()
	model.add(Dense(28, input_dim=n_inputs, kernel_initializer='he_uniform', activation='relu'))
	model.add(Dense(28, input_dim=n_inputs, kernel_initializer='he_uniform', activation='relu'))
	model.add(Dense(28, input_dim=n_inputs, kernel_initializer='he_uniform', activation='relu'))
	model.add(Dense(n_outputs))
	model.compile(loss='mae', optimizer='adam',metrics=['accuracy'])
	return model

 
def evaluate_model(X, y):
	results = list()
	n_inputs, n_outputs = X.shape[1], y.shape[1]
	cv = RepeatedKFold(n_splits=10, n_repeats=5, random_state=1)
	for train_ix, test_ix in cv.split(X):
		X_train, X_test = X[train_ix], X[test_ix]
		y_train, y_test = y[train_ix], y[test_ix]
		model = get_model(n_inputs, n_outputs)
		model.fit(X_train, y_train, verbose=1, epochs=100,batch_size=16)
		mae = model.evaluate(X_test, y_test, verbose=1)
		print('>%.3f' % mae)
		results.append(mae)
	return results

def reset_random_seeds():
   os.environ['PYTHONHASHSEED']=str(1)
   tf.random.set_seed(1)
   np.random.seed(1)
   random.seed(1)

reset_random_seeds()

X, y = get_dataset()
X_mean = mean(X,axis=0)
X_std = std(X,axis=0)
y_mean = mean(y,axis=0)
y_std = std(y,axis=0)

print(X_mean, X_std, y_mean, y_std)

scaler = StandardScaler()
X_train = scaler.fit_transform(X)
y_train = scaler.fit_transform(y)

n_inputs, n_outputs = X.shape[1], y.shape[1]
model = get_model(n_inputs, n_outputs)
model.fit(X_train, y_train, verbose=0, epochs=1000, batch_size=16)

model.save("Model.h5") 
print("Model saved.")

if(input("Evaluate the model?") in ['Y','y','YES','Yes','yes']):
	print("EVALUATING MAE.....")
	results = evaluate_model(X_train, y_train)
	print('MAE: %.3f (%.3f)' % (mean(results), std(results)))