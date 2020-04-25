import requests
import logging
from newsapp.endpoints import INDIA_STATE_WISE_URL,API_KEY_HEADERS,INDIA_COVID_HISTORY_URL


def get_data():
    try:
        response = requests.get(INDIA_STATE_WISE_URL,headers = API_KEY_HEADERS)
        response = response.json()
        
        if response["statusCode"] == "200":
            data = response["response"] 
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
