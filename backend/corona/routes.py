from flask import Blueprint
from flask import request, render_template
from corona.util import get_corona_history, get_state_wise_data_wiki, get_country_wise_data, get_country_summary, get_email_data
from __init__ import mail
from flask_mail import Message

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
