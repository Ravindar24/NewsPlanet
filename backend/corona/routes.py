from flask import Blueprint
from flask import request, render_template
from corona.util import get_corona_history, get_state_wise_data_wiki, get_country_wise_data, get_country_summary, get_email_data
from corona import mail, db
from corona.models import User
from flask_mail import Message
from corona.forms import SubscriptionForm

corona = Blueprint('corona', __name__)

@corona.route("/get-corona-history/v1", methods=["GET"])
def country_covid_history_view():
    data = get_corona_history()
    return ({"data" : data})

@corona.route("/get-indian-states-data/v1", methods=["GET"])
def state_wise_data_wiki():
    data = get_state_wise_data_wiki()
    return ({"data" : data})

@corona.route("/get-countries-data/v1", methods=["GET"])
def country_wise_data_wiki():
    data = get_country_wise_data()
    return ({"data" : data})

@corona.route("/get-country-summary/v1", methods=["GET"])
def country_wise_summary():
    data = get_country_summary()
    return ({"data" : data})

@corona.route("/send-covid-email/v1", methods=["GET"])
def send_email():
    try:
        state_data, country_data = get_email_data()
        if state_data and country_data:
            html_template = render_template("email_template.html", india_data = state_data, country_data = country_data)
            # msg = Message('NewsPlanet: Covid-19 Updates', recipients=[])
            msg = Message('NewsPlanet: Covid-19 Updates', bcc=['']) # recipients here
            msg.html = html_template
            mail.send(msg)
            return {"Result": "Email Sent Successfully"}
        else:
            return {"Result": "Email Data not present"}
    except Exception as ex:
        print("MAIL EXCEPTION",ex)
        return {"Result":"MAIL ERROR"}

@corona.route("/subscribe", methods=["POST"])
def subscribe():
    try:
        form = SubscriptionForm()
        if form.validate_on_submit():
            email = form.email.data
            if email and not User.query.filter_by(email=email).first(): # duplicate emails
                user = User(email=email)
                db.session.add(user)
                db.session.commit()
                print(f"Data in dB {User.query.all()}")
                return ({"data" : "Email Added Successfully"})
            else:
                return ({"data" : "Incorrect Email or Email Alreay Exists"})
        return ({"data" : "Form is not valid"})
    except Exception as ex:
        print("FORM EXCEPTION",ex)
        return ({"data" : "Exception while submitting the form"})
