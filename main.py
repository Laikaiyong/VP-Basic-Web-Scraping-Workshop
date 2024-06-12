from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Firefox()

url = 'https://app.virtuals.io/stake'
driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
images = soup.find_all('img', {"alt": "virtual character"})
names = soup.find_all('p', class_="MuiTypography-root MuiTypography-body1 MuiTypography-noWrap css-yvh85y")


with open('example_data.csv', 'w') as f:
    f.write("Name, Image\n")
    for virtual in zip(names, images):
        print(virtual)
        f.write("{}, {}\n".format(virtual[0].get_text(), virtual[1].get('src')))