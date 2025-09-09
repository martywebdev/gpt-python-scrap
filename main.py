'''its scraping time!'''
import requests
from bs4 import BeautifulSoup


URL = "https://quotes.toscrape.com"


response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

first_quote = soup.select_one('.quote')
# Extract pieces
text = first_quote.select_one(".text").get_text()
author = first_quote.select_one(".author").get_text()
tags = [tag.get_text() for tag in first_quote.select(".tag")]

print("Quote:", text)
print("Author:", author)
print("Tags:", tags)
