from flask import request
from corona.get_corona_data import get_data,get_corona_history, get_state_wise_data_wiki
from newsapp import app

@app.route("/get-corona-data/v1", methods=["GET"])
def covid_view():
    data = get_data()
    return ({"data" : data})

@app.route("/get-corona-history/v1", methods=["GET"])
def country_covid_history_view():
    data = get_corona_history()
    return ({"data" : data})

@app.route("/get-indian-states-data/v1", methods=["GET"])
def state_wise_data_wiki():
    data = get_state_wise_data_wiki()
    return ({"data" : data})

    