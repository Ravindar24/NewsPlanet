import requests
import logging
import pandas as pd
from newsapp.endpoints import INDIA_STATE_WISE_URL,API_KEY_HEADERS,INDIA_COVID_HISTORY_URL, STATE_URL, COUNTRIES_URL


def get_data():
    try:
        response = requests.get(INDIA_STATE_WISE_URL,headers = API_KEY_HEADERS)
        response = response.json()
        
        if response["statusCode"] == "200":
            data = response["response"]
            data = data[0:len(data)-1]
            return data

    except requests.RequestException as E:
        logging.log(str(E))
        return {"ERROR": "Problem with API"}

def get_corona_history():
    try:
        response = requests.get(INDIA_COVID_HISTORY_URL)
        return response.json()

    except requests.RequestException as E:
        logging.log(str(E))
        return {"ERROR": "Problem with API"}

def get_state_wise_data_wiki():
    try:
        table = pd.read_html(STATE_URL)[5][3:40]
        table = table[[1,2,3,4,5]]
        table.columns = ["location", "cases", "deaths", "recovered", "active"]
        state_data = table.to_dict('records')
        logging.info(f" India Example - {state_data[0]}")
        return state_data
        # {'location': 'Andaman and Nicobar Islands', 'cases': '33', 'deaths': '0', 'recovered': '33', 'active': '0'}
    except Exception as ex:
        logging.Exception("Exception in State Wise Wiki API")
        return {"ERROR": "Problem with API"}

def get_country_wise_data_wiki():
    try:
        world_table = pd.read_html(COUNTRIES_URL)[4][0:228]
        world_table.drop([('Locations[e]', '229'), 'Ref.'], axis = 1, inplace=True)
        world_table.columns = ["location", "cases", "deaths", "recovered"]
        world_table_data =  world_table.to_dict(orient = 'records')
        logging.info(f"Countries Example - {world_table_data[0]}")
        return world_table_data
    except Exception as ex:
        logging.Exception("Exception in Country Wise Wiki API")
        return {"ERROR": "Problem with Country Wise Wiki API"}