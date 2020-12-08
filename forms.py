from flask_wtf import FlaskForm
from wtforms import DecimalField,SelectField,RadioField,SubmitField
from wtforms.validators import DataRequired,NumberRange

class UserInput(FlaskForm):
	budget = DecimalField('Budget',validators=[DataRequired(),NumberRange(min=7500,message='Invalid Budget')])
	os = SelectField('Operating System',choices = [('Android','Android'),('iOS','iOS')])
	p1 = RadioField('Enter Your 1st Priority', choices = [(1, 'Browsing Social Media'), (2, 'Watching Videos or Movies')
						,(3, 'Taking Photos And Videos'),(4,'Taking Selfies'),(5,'Gaming'),(6,'Multitasking')])
	p2 = RadioField('Enter Your 2nd Priority', choices = [(1, 'Browsing Social Media'), (2, 'Watching Videos or Movies')
						,(3, 'Taking Photos And Videos'),(4,'Taking Selfies'),(5,'Gaming'),(6,'Multitasking')])
	p3 = RadioField('Enter Your 3rd Priority', choices = [(1, 'Browsing Social Media'), (2, 'Watching Videos or Movies')
						,(3, 'Taking Photos And Videos'),(4,'Taking Selfies'),(5,'Gaming'),(6,'Multitasking')])
	p4 = RadioField('Enter Your 4th Priority', choices = [(1, 'Browsing Social Media'), (2, 'Watching Videos or Movies')
						,(3, 'Taking Photos And Videos'),(4,'Taking Selfies'),(5,'Gaming'),(6,'Multitasking')])
	p5 = RadioField('Enter Your 5th Priority', choices = [(1, 'Browsing Social Media'), (2, 'Watching Videos or Movies')
						,(3, 'Taking Photos And Videos'),(4,'Taking Selfies'),(5,'Gaming'),(6,'Multitasking')])
	submit = SubmitField("Submit")