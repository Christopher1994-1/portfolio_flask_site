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