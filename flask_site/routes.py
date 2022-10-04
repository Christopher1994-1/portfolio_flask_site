import math
from unittest.case import doModuleCleanups
from flask import Flask, render_template, redirect, request, flash, url_for, send_from_directory
# from flask_site.forms import AddingImages, RegistrationForm, LoginForm, AdminLogin, AddingPictures, SearchImages, SearchForm, FamilyForm
from flask_site import app
import os
import requests
import time




######################################################################3
# website routes


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about1.html')
def about1():
    return render_template('about1.html')



@app.route('/contact.html')
def contact():
    return render_template('contact.html')



@app.route('/web_design.html')
def web_design():
    return render_template('web_design.html')