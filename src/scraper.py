import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/the-nightingale_267/index.html"
response = requests.get(url)
print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')

# Searching for book title
title = soup.find("h1") 
print(title.text)