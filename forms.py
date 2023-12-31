from flask_wtf import Form
from wtforms import PasswordField, StringField, SubmitField, validators
from wtforms.fields import EmailField


class RegistrationForm(Form):
    email = EmailField('email', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('password',
                             validators=[
                                 validators.DataRequired(), 
                                 validators.Length(min=8, message="Please choose a password of at least 8 characters")
                                ]
                )
    password2 = PasswordField('password2',
                              validators=[
                                  validators.DataRequired(),
                                  validators.EqualTo('password', message='Passwords must match')
                                ]
                )
    submit = SubmitField('submit', [validators.DataRequired()])

class LoginForm(Form):
    loginemail = EmailField('email', validators=[validators.DataRequired(), validators.Email()])
    loginpassword = PasswordField('password', validators=[validators.DataRequired(message="Password field is required")])
    submit = SubmitField('submit', [validators.DataRequired()])

class CreateTableForm(Form):
    tablenumber = StringField('tablenumber', validators=[validators.DataRequired()])
    submit = SubmitField('createtablesubmit', validators=[validators.DataRequired()])

class DeleteTableForm(Form):
    tableid = StringField('tableid', validators=[validators.DataRequired()])
    submit = SubmitField('deletetablesubmit', validators=[validators.DataRequired()])
