import os
import csv
import requests
from bs4 import BeautifulSoup

# ask the user which URL they wish to get data from
url = input('\nEnter the URL from which to scrape the statistical data\n: ')

# ask the user to specify a directory for the output data file
path = input('\nEnter the absolute path where you would like to save the data set\n:')
if not path:
    path = os.getcwd()
print(f'Saving data set to: {path}')

headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/77.0.3865.90 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

# the following two lines only pull out the header row from the table on the page
# stat_table = soup.find('thead')
# stat_data = stat_table.find_all('tr')

# scrape the stat data and dump it to a file in the same directory
stat_table = soup.find('tbody')
stat_data = stat_table.find_all('tr')

# write the data to a CSV file
with open(os.path.join(path, 'stats.csv'), mode='w', newline='') as stats_file:
    stats_writer = csv.writer(stats_file)
    
    # write the header row
    header_row = ['#', 'Player', 'AVG', 'OPS', 'GP-GS', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'TB', 'SLG%', 'BB', 'HBP', 'SO', 'GDP', 'OB%', 'SF', 'SH', 'SB-ATT']
    stats_writer.writerow(header_row)
    
    # write the data rows
    # for row in stat_data:
    #     stats_writer.writerow([td.text.strip() for td in row.find_all('td')])

    for row in stat_data:
    # Extract the text from each td tag, and exclude "View Bio" if it's present
        row_data = [td.text.strip() for td in row.find_all('td') if td.text.strip() != 'View Bio']
    # Write the row data to the CSV file
        stats_writer.writerow(row_data)

    
print(f'Successfully wrote data to {os.path.join(path, "stats.csv")}')
