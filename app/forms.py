from flask_wtf import Form
from wtforms import TextField, PasswordField, BooleanField, SelectField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Length, Email, EqualTo, Optional
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask.ext.wtf.recaptcha import RecaptchaField
from models import *

class LoginForm(Form):
	email = TextField('email', validators = [InputRequired(), Email()])
	password =  PasswordField('password', validators = [InputRequired()])
	remember_me = BooleanField('remember_me', default = True)

class EditForm(Form):	
	password =  PasswordField('password', validators = [InputRequired(), EqualTo('password_confirm', message='Passwords must match')])
	password_confirm =  PasswordField('password_confirm', validators = [InputRequired()])

class SubmitForm(Form):
	problem_id = TextField('problem_id', validators = [InputRequired()])
	language = SelectField('language', choices = [(C, 'C'), (CPP, 'C++'), (PYTHON, 'Python')], validators = [InputRequired()], coerce=int)
	upload_file = FileField('upload_file', validators=[FileRequired()])

class SignupForm(Form):
	email = TextField('email', validators = [InputRequired(), Email()])
	nickname = TextField('nickname', validators = [InputRequired()])
	password =  PasswordField('password', validators = [InputRequired(), EqualTo('password_confirm', message='Passwords must match')])
	password_confirm =  PasswordField('password_confirm', validators = [InputRequired()])
	role = SelectField('role', choices = [(ROLE_USER, 'user'), (ROLE_ADMIN, 'admin')], validators = [InputRequired()], coerce=int)

class PostForm(Form):
	problem_id = IntegerField('problem_id', validators = [InputRequired()])
	title = TextField('title', validators = [InputRequired(), Length(max = 100)])
	time_limit = IntegerField('time_limit', validators = [InputRequired()])
	memory_limit = IntegerField('time_limit', validators = [InputRequired()])
	description = TextAreaField('description', validators = [InputRequired()])
	input_description = TextAreaField('input_description', validators = [InputRequired()])
	output_description = TextAreaField('output_description', validators = [InputRequired()])
	input_sample = TextAreaField('input_sample', validators = [InputRequired()])
	output_sample = TextAreaField('output_sample', validators = [InputRequired()])
	hint = TextAreaField('hint', validators = [Optional()])
