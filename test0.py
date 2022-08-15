import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = 'https://tarletonsports.com/sports/baseball/stats/2022'

# ask the user to specify a directory for the output data file
#path = input(
    #'\nEnter the absolute path where you would like to save the data set\n:')

headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/77.0.3865.90 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

def player_names():
    name_table = soup.find('tbody')
    name_data = name_table.find_all('a', class_='hide-on-medium-down')

    clean_names = re.findall('(?<=>).*?(?=<)', str(name_data))

    return clean_names 


print(player_names())
