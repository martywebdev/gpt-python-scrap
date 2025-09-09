'''its scraping time!'''
import requests
from bs4 import BeautifulSoup


URL = "https://quotes.toscrape.com"


response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

first_quote = soup.select_one('.quote')
print(first_quote.prettify())
