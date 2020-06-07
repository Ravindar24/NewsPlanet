from flask import request
from corona.get_corona_data import get_corona_history, get_state_wise_data_wiki, get_country_wise_data, get_country_summary
from newsapp import app

@app.route("/get-corona-history/v1", methods=["GET"])
def country_covid_history_view():
    data = get_corona_history()
    return ({"data" : data})

@app.route("/get-indian-states-data/v1", methods=["GET"])
def state_wise_data_wiki():
    data = get_state_wise_data_wiki()
    return ({"data" : data})

@app.route("/get-countries-data/v1", methods=["GET"])
def country_wise_data_wiki():
    data = get_country_wise_data()
    return ({"data" : data})

@app.route("/get-country-summary/v1", methods=["GET"])
def country_wise_summary():
    data = get_country_summary()
    return ({"data" : data})