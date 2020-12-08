from flask import Flask, render_template, flash, request, jsonify, url_for, redirect
from recommender import Recommender, update
from forms import UserInput
import webbrowser

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/",methods = ['GET', 'POST'])
@app.route("/home",methods = ['GET', 'POST'])
def home():
	form = UserInput()
	if request.method == 'POST':
		data = request.form
		r = Recommender()
		results = r.recommend(data)
		print(results)
		return render_template('results.html',results=results)
	return render_template('home.html',form=form)

@app.route("/about")
def about():
	return render_template('about.html')	

@app.route("/results/<index>/<link>")
def results(index=None,link=None):
	update(index)
	print("ENTER\n\n\n\n\n\n\n\n\n\n\n\n")
	return webbrowser.open_new_tab(link)

if __name__=='__main__':
	app.run(debug=True)