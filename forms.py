from flask_wtf import FlaskForm
from wtforms import DecimalField,SelectField,RadioField,SubmitField
from wtforms.validators import DataRequired, NumberRange, ValidationError

class UserInput(FlaskForm):
	budget = DecimalField('Budget',validators=[DataRequired(),NumberRange(min=7500,message='Please enter a value above Rs.7500')])
	os = SelectField('Operating System',choices = [('Android','Android'),('iOS','iOS')],validators=[DataRequired()])
	p1 = RadioField('Enter Your 1st Priority', choices = [(1, 'Browsing Social Media'), (2, 'Watching Videos or Movies')
						,(3, 'Taking Photos And Videos'),(4,'Taking Selfies'),(5,'Gaming'),(6,'Multitasking')],validators=[DataRequired()])
	p2 = RadioField('Enter Your 2nd Priority', choices = [(1, 'Browsing Social Media'), (2, 'Watching Videos or Movies')
						,(3, 'Taking Photos And Videos'),(4,'Taking Selfies'),(5,'Gaming'),(6,'Multitasking')],validators=[DataRequired()])
	p3 = RadioField('Enter Your 3rd Priority', choices = [(1, 'Browsing Social Media'), (2, 'Watching Videos or Movies')
						,(3, 'Taking Photos And Videos'),(4,'Taking Selfies'),(5,'Gaming'),(6,'Multitasking')],validators=[DataRequired()])
	p4 = RadioField('Enter Your 4th Priority', choices = [(1, 'Browsing Social Media'), (2, 'Watching Videos or Movies')
						,(3, 'Taking Photos And Videos'),(4,'Taking Selfies'),(5,'Gaming'),(6,'Multitasking')],validators=[DataRequired()])
	p5 = RadioField('Enter Your 5th Priority', choices = [(1, 'Browsing Social Media'), (2, 'Watching Videos or Movies')
						,(3, 'Taking Photos And Videos'),(4,'Taking Selfies'),(5,'Gaming'),(6,'Multitasking')],validators=[DataRequired()])
	submit = SubmitField("Submit")

	def validate_p5(self,p5):
		if p5.data in [self.p1.data,self.p2.data,self.p3.data,self.p4.data]:
			raise ValidationError("You have already chosen this priority!")
	def validate_p4(self,p4):
		if p4.data in [self.p1.data,self.p2.data,self.p3.data]:
			raise ValidationError("You have already chosen this priority!")
	def validate_p3(self,p3):
		if p3.data in [self.p1.data,self.p2.data]:
			raise ValidationError("You have already chosen this priority!")
	def validate_p2(self,p2):
		if p2.data in [self.p1.data]:
			raise ValidationError("You have already chosen this priority!")





