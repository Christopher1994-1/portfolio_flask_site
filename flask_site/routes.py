import math
from unittest.case import doModuleCleanups
from flask import Flask, render_template, redirect, request, flash, url_for, send_from_directory, jsonify
from flask_site.forms import ContactMe
from flask_site import app
import os
import requests
import time
import smtplib
import json



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





def api_response(prompt, tokens, temp):
    import openai
    """
    Generates a text response based on a given prompt using the OpenAI API.
    
    Parameters:
        prompt (str): The text prompt that the API will use as the starting point for generating a response.
    
    Returns:
        str: The generated text response.
        
    Example:
        response = api_response("What is the weather like today?")
        print(response)
        # Output: "The weather today is sunny with a high of 75 degrees."
    """
    # Use your API key
    openai.api_key = os.environ.get("OpenAI_Key")

    
    
    if tokens == 0:
        tokens = 100
    
        


    model_response = str(openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=tokens,
    temperature=temp
    ))
    json_obj = json.loads(model_response)
    response = json_obj["choices"][0]["text"]
    return response








home_page = []

under_maintenance = False

##############################################################################
# website routes


# Maintenance page ~
@app.route('/maintenance1.html')
def maintenance1():
    return render_template('maintenance1.html')

# Home page
@app.route('/')
def index():
    global home_page
    if len(home_page) > 0:
        home_page = []
        home_page.append(1)
    else:
        home_page.append(1)
    
    if under_maintenance:
        return render_template('maintenance1.html')
    else:
        return render_template('index.html')






# The about page
@app.route('/about1.html')
def about1():
    
    if under_maintenance:
        return render_template('maintenance1.html')
    else:
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
    
    if under_maintenance:
        return render_template('maintenance1.html')
    else:
        return render_template('/contact.html', form=form)


# dropdown website design
@app.route('/web_design.html')
def web_design():
    global home_page
    if len(home_page) > 0:
        home_page = []
        home_page.append(0)
        
    if under_maintenance:
        return render_template('maintenance1.html')
    else:
        return render_template('/web_design.html')


# dropdown backend web
@app.route('/backend_web.html')
def backend_web():
    if under_maintenance:
        return render_template('maintenance1.html')
    else:
        return render_template('/backend_web.html')


# dropdown programming
@app.route('/programming.html')
def programming():
    
    if under_maintenance:
        return render_template('maintenance1.html')
    else:
        return render_template('/programming.html')


# resume route
@app.route('/resume.html')
def resume():
    if under_maintenance:
        return render_template('maintenance1.html')
    else:
        return render_template('/resume.html')


# contacts page
@app.route('/contacts_gui.html')
def contacts_gui():
    if under_maintenance:
        return render_template('maintenance1.html')
    else:
        return render_template('/contacts_gui.html')








# Programming Projects ~ Full Calcualtor ~
@app.route('/full_calculator.html')
def full_calculator():
    images = {"https://raw.githubusercontent.com/Christopher1994-1/full_calculator_gui_oop/main/images/standard_look.png": "This is the standard option of the calculator which is the dafault option. It does the basic calculations you would expect from a calculator.",
              "https://raw.githubusercontent.com/Christopher1994-1/full_calculator_gui_oop/main/images/standard_look_switch.png": "The calculator has some options on the menu bar so the user can easily go between the four options the calculator provides.",
              "https://raw.githubusercontent.com/Christopher1994-1/full_calculator_gui_oop/main/images/advanced_look.png": "This is the advanced option of the calculator. In this option you can do more advanced calculations including finding the square root of a number, the mod and expont.",
              "https://raw.githubusercontent.com/Christopher1994-1/full_calculator_gui_oop/main/images/currency_exchange_look.png": "This is the currency exchange option, I am using the ExchangeRate API for up to date rates. The user types in a number in the first 0 input and which ever currency they have selected.",
              "https://raw.githubusercontent.com/Christopher1994-1/full_calculator_gui_oop/main/images/temp_look.png":"Finally, this is the temperature converter option, much like the currency exchange option and the same layout but without the use of an API and just some standard class methods to do the convertering.",
              }
    if under_maintenance:
        return render_template('maintenance1.html')
    else:
        return render_template('/full_calculator.html', images=images)



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


# Website Demo Project ~ Tattoo Website ~
@app.route('/web_scrap.html')
def web_scrap():
    images = ["A easy automated web scraping python script that helps me stay up to date with my favorite grocery store deals"]
    return render_template('web_scrap.html', images=images)



# ++

# Website Route for the Fast Food Live Demo
@app.route("/subway_live_demo")
def subway():
    return render_template('subway/index.html')


# Website Route for about Subway website
@app.route("/about_subway")
def about_subway():
    return render_template('about_subway.html')



# Website Route for second web design page
@app.route("/web_design_page_two")
def web_design_two():
    return render_template('web_design_two.html')





# Website Route for Fast Food Live Demo
@app.route("/fast_food_website")
def fast_food():
    return render_template('fast_food/fast_food_live_demo.html')


# Website Route for about Fast Food website
@app.route("/about_restaurant")
def about_restaurant():
    return render_template('about_restaurant.html')




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


# Website Design Projects ~ UFO Site ~
@app.route('/ufo_site.html')
def ufo_site():
    return render_template('ufo_site.html')


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


# Website Design Projects ~ Dentist Site ~
@app.route('/dentist_about.html')
def dentist_about():
    return render_template('dentist_about.html')





# Page for the BigFoot Dataset website
@app.route('/bigfoot_site')
def bigfoot_site():
    return render_template('bigfoot_site.html')



# Page for the Contributions dropdown page
@app.route('/contributions')
def contributions():
    return render_template('contributions.html')



# Page for the contrbutions/commits - python clock
@app.route('/commits/python_clock')
def python_clock():
    project_name = "Python Clock"
    commits = {'#060e4a5': ['https://github.com/JohnRick120/Python_Clock/commit/060e4a5cd0bda97ffedec4d0af0a625f7e6155de', 'added datetime var, months dict, new layout.'],
               "#5c1d8d3": ['https://github.com/JohnRick120/Python_Clock/commit/5c1d8d3f72fd82bdf9270df1249a7b1f2fadef9a', 'updated read me.'],
               "#729524c": ['https://github.com/JohnRick120/Python_Clock/commit/729524c1bd64626808db938e6b43f21bc850ed8d', 'finshed update method and added readme image.'],}
    return render_template('commits.html', project_name=project_name, commits=commits)



# Page for the contributions/commits - weatherapp
@app.route('/commits/weatherapp')
def weatherapp():
    project_name = "WeatherApp"
    commits = {
        "#c3756a1": ['https://github.com/Christopher1994-1/WeatherApp/commit/c3756a1dad670ce85f9ecb4ba1e85d386250cb65', 'updated README.md'],
        "#661037e": ['https://github.com/Christopher1994-1/WeatherApp/commit/661037e787d2c274c4aed26a9310a730aa638166','changed capitalize() method to title() method']
    }
    return render_template('commits.html', project_name=project_name, commits=commits)




# Website Demo Project ~ Starbucks Website ~
@app.route('/starbucks_website.html')
def starbucks_website():
    value = home_page[0]
    return render_template('starbucks_website.html', value=value)




# Website Demo Project ~ ChatGPT Replica ~
@app.route('/chat_demo.html', methods=["GET", "POST"])
def chat_demo():
    # example prompts
    example_prompt_one = "Explain quantum computing in simple terms"
    example_prompt_two = "Got any creative ideas for a 10 year old's birthday?"
    example_prompt_three = "How do I make an HTTP request in JavaScript?"
    return render_template('chat_demo.html', 
                           example_prompt_one=example_prompt_one,
                           example_prompt_two=example_prompt_two,
                           example_prompt_three=example_prompt_three)

@app.route('/about_chat.html')
def about_chat():
    images = ["A easy automated web scraping python script that helps me stay up to date with my favorite grocery store deals"]
    return render_template('about_chat.html')



@app.route('/my_backend_endpoint', methods=['POST'])
def my_backend_function():
    input_text = request.json.get('text')
    temp = request.json.get('temp')
    tokens = int(request.json.get('tokens'))
    
    if temp == "0":
        temp = 0.9
    else:
        temp = float(temp)
        
    api = api_response(input_text, tokens, temp)
    return jsonify({'result': api})




# Website Demo Project ~ Tattoo Website ~
@app.route('/tattoo_mock.html')
def tattoo_mock():
    return render_template('tattoo_mock.html')



# Website Demo Project ~ Dentist ~
@app.route('/dentist.html')
def dentist():
    return render_template('dentist.html')



# Website Route ~ Certificates ~
@app.route('/certificates.html')
def certificates():
    return render_template('certificates.html')


#test route
@app.route('/test.html')
def test():
    images = ["command 1", "command 2"]
    return render_template('test.html', images=images)



