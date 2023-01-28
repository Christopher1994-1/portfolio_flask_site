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


# dropdown website design
@app.route('/web_design.html')
def web_design():
    return render_template('web_design.html')


# dropdown backend web
@app.route('/backend_web.html')
def backend_web():
    return render_template('backend_web.html')


# dropdown programming
@app.route('/programming.html')
def programming():
    return render_template('programming.html')


# resume route
@app.route('/resume.html')
def resume():
    return render_template('resume.html')


# contacts page
@app.route('/contacts_gui.html')
def contacts_gui():
    return render_template('contacts_gui.html')








# Programming Projects ~ Full Calcualtor ~
@app.route('/full_calculator.html')
def full_calculator():
    images = {"https://raw.githubusercontent.com/Christopher1994-1/full_calculator_gui_oop/main/images/standard_look.png": "This is the standard option of the calculator which is the dafault option. It does the basic calculations you would expect from a calculator.",
              "https://raw.githubusercontent.com/Christopher1994-1/full_calculator_gui_oop/main/images/standard_look_switch.png": "The calculator has some options on the menu bar so the user can easily go between the four options the calculator provides.",
              "https://raw.githubusercontent.com/Christopher1994-1/full_calculator_gui_oop/main/images/advanced_look.png": "This is the advanced option of the calculator. In this option you can do more advanced calculations including finding the square root of a number, the mod and expont.",
              "https://raw.githubusercontent.com/Christopher1994-1/full_calculator_gui_oop/main/images/currency_exchange_look.png": "This is the currency exchange option, I am using the ExchangeRate API for up to date rates. The user types in a number in the first 0 input and which ever currency they have selected.",
              "https://raw.githubusercontent.com/Christopher1994-1/full_calculator_gui_oop/main/images/temp_look.png":"Finally, this is the temperature converter option, much like the currency exchange option and the same layout but without the use of an API and just some standard class methods to do the convertering.",
              }
    return render_template('full_calculator.html', images=images)



# Programming Projects ~ Password GUI ~
@app.route('/password_gui.html')
def password_gui():
    return render_template('password_gui.html')



# Programming Projects ~ Desktop Assistant ~
@app.route('/desktop_assistant.html')
def desktop_assistant():
    images = [
        "Command: 'go to chess.com' Opens a new window that goes to the specified website.", 
        "Command: what time is it?, or what's the time? When this command is heard it calls a simple function that tells you the current time.",
        "Command: what are, who is, what is a, who are the, what is the - ? This command takes a question you have of something and uses the Wikipedia module and reads off the first two sentences of information.",
        "Command: How is the weather in - ? Given this command is a city name, it will look up the current weather of that city using the OpenWeatherMap API.",
        "Command: what is the weather outside?, how is it outside?, what's the weather? This command is much like the last weather command but instead this one returns your citys current weather.",
        "Command: Write This Down, This command opens notepad app and then listens for input to write down what you say and save it to notepad",
        "Command: How do you spell - ? This command is another super simple one, when this is triggered it takes the word you want to spell and repeats which character of the word back to you.",
        "Command: what is today's date? This commands is a simple one that when called tells back the date to the user.",
        "Command: You can text to contacts",
        ]
    return render_template('desktop_assistant.html', images=images)



# Programming Projects ~ OpenAi GUI ~
@app.route("/openai.html")
def openai():
    images = ["I developed a GUI using Python Tkinter that intergrated OpenAI API that returns a response to a user input"]
    return render_template("/openai.html", images=images)



# Website Design Projects ~ Archive Site ~
@app.route('/archive_site.html')
def archive_site():
    return render_template('archive_site.html')

# Website Design Projects ~ Weather Site ~
@app.route('/weather_site.html')
def weather_site():
    return render_template('weather_site.html')

# Website Design Projects ~ Investor Site ~
@app.route('/investor_site.html')
def investor_site():
    return render_template('investor_site.html')

# Website Design Projects ~ Smoke Shop ~
@app.route('/smoke_shop.html')
def smoke_shop():
    return render_template('smoke_shop.html')

# Website Design Projects ~ Starbucks Site ~
@app.route('/starbucks_site.html')
def starbucks_site():
    return render_template('starbucks_site.html')


# Website Design Projects ~ Tattoo Shop ~
@app.route('/tattoo_shop.html')
def tattoo_shop():
    return render_template('tattoo_shop.html')




#test route
@app.route('/test.html')
def test():
    images = ["command 1", "command 2"]
    return render_template('test.html', images=images)



