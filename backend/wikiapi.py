# # BS4 
# import requests
# from bs4 import BeautifulSoup

# page = requests.get("https://en.wikipedia.org/wiki/List_of_companies_of_Indonesia")
# soup = BeautifulSoup(page.content, 'html.parser')
# ta = soup.find_all('table',class_="wikitable")

# print(ta)

# Pandas
import pandas as pd

# Indian State Data
url = "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_India"
table = pd.read_html(url)[5][3:40]
table = table[[1,2,3,4,5]]
table.columns = ["location", "cases", "deaths", "recovered", "active"]
state_data = table.to_dict('recods')
print(f" India Example - {state_data[0]}")

# Global Contries Data
global_url = "https://en.wikipedia.org/wiki/COVID-19_pandemic"
world_table = pd.read_html(global_url)[4][0:228]
world_table.drop([('Locations[e]', '229'), 'Ref.'], axis = 1, inplace=True)
world_table.columns = ["location", "cases", "deaths", "recovered"]
world_table_data =  world_table.to_dict(orient = 'records')
print(f"Countries Example - {world_table_data[0]}")