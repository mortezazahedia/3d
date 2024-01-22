from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length , NumberRange, Email, EqualTo, ValidationError
from easystudy.models import User
from flask_wtf.file import FileField, FileAllowed, FileRequired

class Register(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(min=3,max=30)])
    age = IntegerField('age', validators=[DataRequired(), NumberRange(min=0,max=99)])
    def validate_age(self, age_from_form):
        if int(age_from_form.data) == 33:
            raise ValidationError('33 is not valid')

    email = StringField('email', validators=[DataRequired(), Email()])
    def validate_email(self, email_from_form):
        result=User.query.filter_by(email=email_from_form.data).first()
        if result:
            raise ValidationError('email address is already registered')

    gender = SelectField('Gender', choices=[('man', 'Man'), ('woman', 'Woman'), ('both', 'Both'), ('unknown', 'Unknown')])
    
    password = PasswordField('password', validators=[DataRequired()])
    confirmpassword = PasswordField('confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up', validators=[DataRequired()])


class Login(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')
    remember = BooleanField('Remember me')


class Account(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(min=3, max=30)])
    age = IntegerField('age', validators=[DataRequired(), NumberRange(min=0, max=99)])

    def validate_age(self, age_from_form):
        if int(age_from_form.data) == 33:
            raise ValidationError('33 is not valid')

    email = StringField('email', validators=[DataRequired(), Email()])
    profile_pic = FileField('profile_pic',validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])

    gender = SelectField('Gender',
                         choices=[('man', 'Man'), ('woman', 'Woman'), ('both', 'Both'), ('unknown', 'Unknown')])

    submit = SubmitField('Updates Detailes', validators=[DataRequired()])