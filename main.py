import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Firefox()

url = 'https://app.virtuals.io/stake'
# response = requests.get(url)
# print(response.content)
driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
images = soup.find_all('img', {"alt": "virtual character"})
names = soup.find_all('p', class_="MuiTypography-root MuiTypography-body1 MuiTypography-noWrap css-yvh85y")
virtuals = soup.find_all('p', class_="MuiTypography-root MuiTypography-body1 css-6d7ygw")


with open('example_data.csv', 'w') as f:
    f.write("Name, Image, Virtuals\n")
    for virtual in zip(names, images, virtuals):
        f.write("{}, {}, {}\n".format(virtual[0].get_text(), virtual[1].get('src'), virtual[2].get_text().replace(",", "")))