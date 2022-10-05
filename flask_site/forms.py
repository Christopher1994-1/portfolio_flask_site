import email
from genericpath import exists
from logging import PlaceHolder
from math import remainder
from xml.dom import ValidationErr
from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators, FileField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, email_validator, ValidationError
import email_validator
import mysql.connector
import os
# from flask_site.models import Members, Images


# class for contact me page
class ContactMe(FlaskForm):
    first_name = StringField("First Name:", validators=[DataRequired()], render_kw={"placeholder": "Required"})
    last_name = StringField("Last Name:", render_kw={"placeholder": "Optional"})
    company = StringField("Company:", render_kw={"placeholder": "Optional"})
    email = StringField("Email", validators=[DataRequired(), validators.Email()], render_kw={"placeholder": "Required"})
    message = TextAreaField("Message:", validators=[DataRequired()], render_kw={"placeholder": "Required"})
    submit = SubmitField("Submit")
