import math
from unittest.case import doModuleCleanups
from flask import Flask, render_template, redirect, request, flash, url_for, send_from_directory
from flask_site.forms import ContactMe
from flask_site import app
import os
import requests
import time
import smtplib



##############################################################################
# functions
default_value = "None Given"

def send_email(first_name, last_name=default_value, company=default_value, email=default_value, message=default_value):
    my_pass = os.environ.get('ggg')
    my_email = "cejvanniekirk098@gmail.com"
    receiver = "kirko190255@gmail.com" # TODO change to os after restart
    message = f"""New employer is contacting you.\n\nEmployer Information:\n\nName: {first_name} {last_name}\n\nCompany: {company}\n\nMessage:\n{message}"""

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(my_email, my_pass)
        subject = "New Employer!"
        body = message

        msg = f"Subject: {subject}\n\n{body}"

        smtp.sendmail(my_email, receiver, msg)



##############################################################################
# website routes

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# The about page
@app.route('/about1.html')
def about1():
    return render_template('about1.html')


# contact page
@app.route('/contact.html', methods=["POST", "GET"])
def contact():
    form = ContactMe()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        company = form.company.data
        email = form.email.data
        message = form.message.data
        send_email(first_name, last_name, company, email, message)
        flash('Email has been sent')
        return redirect(url_for("contact"))
    return render_template('contact.html', form=form)



@app.route('/web_design.html')
def web_design():
    return render_template('web_design.html')


@app.route('/full_calculator.html')
def full_calculator():
    return render_template('full_calculator.html')


@app.route('/archive_site.html')
def archive_site():
    return render_template('archive_site.html')


@app.route('/weather_site.html')
def weather_site():
    return render_template('weather_site.html')


@app.route('/investor_site.html')
def investor_site():
    return render_template('investor_site.html')


@app.route('/programming.html')
def programming():
    return render_template('programming.html')



@app.route('/desktop_assistant.html')
def desktop_assistant():
    return render_template('desktop_assistant.html')


@app.route('/password_gui.html')
def password_gui():
    return render_template('password_gui.html')


@app.route('/contacts_gui.html')
def contacts_gui():
    return render_template('contacts_gui.html')


# resume route
@app.route('/resume.html')
def resume():
    return render_template('resume.html')



#test route
@app.route('/test.html')
def test():
    return render_template('test.html')


