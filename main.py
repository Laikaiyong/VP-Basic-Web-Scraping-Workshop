import requests
from bs4 import BeautifulSoup


url = 'https://solscan.io/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
links = soup.find_all('a')

for link in links:
    print(link.get('href'))

with open('example_data.csv', 'w') as f:
    for link in links:
        f.write(link.get('href'))
        f.write("\n")