from bs4 import BeautifulSoup
import requests



URL ="https://quotes.toscrape.com"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# scraping the first quote

first_quote = soup.select_one('.quote')

# print(first_quote.prettify())

text = first_quote.select_one('.text').getText()
author = first_quote.select_one('.author').getText()
tags = [tag.get_text() for tag in first_quote.select('.tag')]

print(f"Quote: {text}\nAuthor: {author}\nTags: {tags}")

