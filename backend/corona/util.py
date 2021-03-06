import requests
import logging
import sys
from threading import Thread
import time
import pandas as pd
from corona.corona_api_urls import STATE_URL
import re
from covid import Covid

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
COUNTRY_SUMMARY = {}
STATE_SUMMARY = {}
CACHE_STATE_DATA = []
CACHE_COUNTRY_DATA = []
covid = Covid(source="worldometers")

def clear_cache_thread():
    global CACHE_STATE_DATA, CACHE_COUNTRY_DATA, COUNTRY_SUMMARY
    reset_cache_timer = 0
    logging.info("CACHING DATA INITIALLY") 
    CACHE_STATE_DATA = get_state_wise_data_wiki()
    CACHE_COUNTRY_DATA = get_country_wise_data()
    while True:
        if reset_cache_timer < 1800: # refresh every one hour, todo: add hardcoded data to config files
            reset_cache_timer += 1
            time.sleep(1)
        elif reset_cache_timer == 1800:
            logging.info("REFRESHING CACHE")
            reset_cache_timer = 0
            COUNTRY_SUMMARY = {}
            STATE_SUMMARY = {}
            CACHE_STATE_DATA = []
            CACHE_COUNTRY_DATA = []
            CACHE_STATE_DATA = get_state_wise_data_wiki()
            CACHE_COUNTRY_DATA = get_country_wise_data()

def get_corona_history():
    try:
        # response = requests.get(INDIA_COVID_HISTORY_URL)
        if CACHE_STATE_DATA or STATE_SUMMARY:
            return {"Confirmed":STATE_SUMMARY['cases'], "Recovered":STATE_SUMMARY['recovered'],"Deaths":STATE_SUMMARY["deaths"], "Active":STATE_SUMMARY["active"]}

        return {"ERROR": "Data not Cached Yet"}

    except requests.RequestException as E:
        logging.log(str(E))
        return {"ERROR": "Problem with API"}

def get_state_wise_data_wiki():
    global CACHE_STATE_DATA, STATE_SUMMARY
    try:
        if CACHE_STATE_DATA:
            logging.info("FETCHING FROM CACHED DATA")
            return CACHE_STATE_DATA
        table = pd.read_html(STATE_URL, match = re.compile(r".*Total Confirmed cases.*"))
        table = table[0][0:37]
        table.columns = ["S.No","location", "active", "recovered", "deaths", "cases"]
        state_data = table.to_dict('records')
        STATE_SUMMARY = state_data[-1]
        state_data = state_data[0:35]
        logging.info(f" India Example - {state_data[0]}")
        # state_data = clean_json_data(state_data)
        CACHE_STATE_DATA = state_data
        return state_data
        return {"ERROR": "Couldn't find data in Wiki Tables"}
        # {'location': 'Andaman and Nicobar Islands', 'cases': '33', 'deaths': '0', 'recovered': '33', 'active': '0'}
    except Exception as ex:
        logging.error("Exception in State Wise Wiki API--->",ex)
        return {"ERROR": "Problem with API"}

def get_country_wise_data():
    global CACHE_COUNTRY_DATA, COUNTRY_SUMMARY
    try:
        if CACHE_COUNTRY_DATA:
            logging.info("FETCHING FROM CACHED DATA")
            return CACHE_COUNTRY_DATA
        country_data = []
        data = covid.get_data() # Decimal values causing issues, taking only required data
        for country in data:
            if country["country"].lower() == "world":  # for summary data
                COUNTRY_SUMMARY.update({"TotalConfirmed":country["confirmed"],"TotalRecovered":country["recovered"],"TotalDeaths":country["deaths"], "ActiveCases":country['active']})
            elif not country['country'].isdigit():
                country_data.append({"location":country["country"],"cases":country["confirmed"],"recovered":country["recovered"],"deaths":country["deaths"]})
        CACHE_COUNTRY_DATA = country_data
        return country_data
        # ["country", "confirmed", "deaths", "recovered", "active"]
    except Exception as ex:
        logging.error("Exception in Country Wise Wiki API--->",ex)
        return {"ERROR": "Problem with Country Wise Wiki API"}

def get_country_summary():
    try:
        if COUNTRY_SUMMARY:
            return COUNTRY_SUMMARY
        return {"ERROR": "Data not Cached Yet"}
    except requests.RequestException as E:
        logging.log(str(E))
        return {"ERROR": "Problem with API"}

def clean_json_data(data):
    """Removes Special Characters and Ablphabets from numbers"""
    for entry in data:
        entry['cases'] = re.sub('[^0-9]+', '',entry['cases'])
        entry['deaths'] = re.sub('[^0-9]+', '',entry['deaths'])
        entry['recovered'] = re.sub('[^0-9]+', '',entry['recovered'])
        if entry.get("active", None):  # Active not in Global
            entry["active"] = re.sub('[^0-9]+', '',entry.get("active", ""))
    return data

def get_email_data():
    if CACHE_STATE_DATA and COUNTRY_SUMMARY:
        return [CACHE_STATE_DATA[-1]], [COUNTRY_SUMMARY]
    else:
        return None, None
