import requests
from bs4 import BeautifulSoup

URL = 'https://tarletonsports.com/sports/baseball/stats/2019'

headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/77.0.3865.90 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

# the following two lines only pull out the header row from the table on the page
# stat_table = soup.find('thead')
# stat_data = stat_table.find_all('tr')

stat_table = soup.find('tbody')
stat_data = stat_table.find_all('tr')

print(stat_data, file=open('output.txt', 'w'))