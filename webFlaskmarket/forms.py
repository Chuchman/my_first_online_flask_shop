from cProfile import label
from tkinter import S
from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import length, EqualTo, Email, DataRequired
 

class RegisterForm(FlaskForm):
    username = StringField(label='User Name', validators=[length(min=2,max=35), DataRequired()])
    email_address = StringField(label='Email Address', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:',validators=[length(min=7), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class FeedbackForm(FlaskForm):
    username = StringField(label='Your name', validators=[length(min=2,max=35), DataRequired()])
    email_adress = StringField(label='Email Address', validators=[Email(), DataRequired()])
    message = TextAreaField(label='Your order', validators=[length(min=4, max=300), DataRequired()])
    submit = SubmitField(label='Send your message')