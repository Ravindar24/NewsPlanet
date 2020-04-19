import requests

def get_data():
    response = requests.get("https://api.covid19api.com/countries")
    if response.status_code == 200:
        return {"Countries" : [d['Country'] for d in response.json()]}
    return { "ERROR" : "Problem with API"}
