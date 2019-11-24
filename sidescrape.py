import requests
from bs4 import BeautifulSoup

# ask the user which URL they wish to get data from
#URL = 'https://tarletonsports.com/sports/baseball/stats/2019'
url = input('\nEnter the URL from which to scrape the statistical data\n: ')

#ask the user to specify a directory for the output data file
path = input('\nEnter the absolute path where you would like to save the data set\n:')

headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/77.0.3865.90 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

# the following two lines only pull out the header row from the table on the page
# stat_table = soup.find('thead')
# stat_data = stat_table.find_all('tr')


#scrape the stat data and dump it to a file in the same directory
stat_table = soup.find('tbody')
stat_data = stat_table.find_all('tr')

print(stat_data, file=open(path, 'w'))