# basic_scrape
from bs4 import BeautifulSoup
import requests

url = requests.get('https://quotes.toscrape.com/')

soup = BeautifulSoup(url.text, 'html.parser')

quotes = soup.findAll('span', attrs={'class':'text'})

authors = soup.findAll('small', attrs={'class':'author'})

for quote, author in zip(quotes, authors):
    author_text = author.text if author else 'Unknown Author'
    print(quote.text + " - " + author_text)