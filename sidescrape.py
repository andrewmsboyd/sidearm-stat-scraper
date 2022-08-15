import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# ask the user which URL they wish to get data from
#url = input('\nEnter the URL from which to scrape the statistical data\n: ')
url = 'https://tarletonsports.com/sports/baseball/stats/2022'

# ask the user to specify a directory for the output data file
#path = input(
    #'\nEnter the absolute path where you would like to save the data set\n:')

headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/77.0.3865.90 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

# the following two lines only pull out the header row from the table on the page
# THIS WORKS
def header_data():
    head_table = soup.find('thead')
    head_data = head_table.find_all('tr')

    clean_headers = re.findall('(?<=>).*(?=<)', str(head_data))

    return clean_headers

# function to get just the player's name
def player_names():
    name_table = soup.find('tbody')
    name_data = name_table.find_all('a')

    clean_names = re.findall('(?<=>).*(?=<)', str(name_data))

    return clean_names


# scrape the stat data and dump it to a file in the same directory
#stat_table = soup.find('tbody')
#stat_data = stat_table.find_all('tr')

def stat_data():
    stat_table = soup.find('tbody')
    stat_data = stat_table.find_all('td')

    clean_stats = re.findall('(?<=>).*(?=<)', str(stat_data))

    return clean_stats

# read the player uid
#player_table = soup.find('thead')
#player_ids = player_table.find_all(attrs{'data-player-id': '*'})


#print(header_data()), file = open(path, 'w')
#print(stat_data(), file = open(path, 'w')
print(header_data())
print(player_names())
print(stat_data())
