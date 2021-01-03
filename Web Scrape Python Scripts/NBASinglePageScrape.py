from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
# The NBA champions from 1983 to 2020
url = "https://www.basketball-reference.com/playoffs/"

# collect HTML data
html = urlopen(url)

# Create beautiful soup object
soup = BeautifulSoup(html, "html.parser")

# getText()to extract the headers into a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]

# Get all the rows from table
rows = soup.findAll('tr')[2:]
rows_data = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]

# Remove the empty row
rows_data.pop(20)
rows_data = rows_data[0:38]

# Add the years into rows_data
last_year = 2020
for i in range(0, len(rows_data)):
    rows_data[i].insert(0, last_year)
    last_year -=1

# Create the dataframe
nba_finals = pd.DataFrame(rows_data, columns = headers)
# Export dataframe to a CSV file
nba_finals.to_csv("NBAFinalsChampions.csv", index=False)
