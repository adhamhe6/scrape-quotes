# basic_scrape_csv_export
from bs4 import BeautifulSoup
import requests
import csv

file = open('csv/scraped_quotes1.csv', 'w', encoding='utf-8')
writer = csv.writer(file)

writer.writerow(['Quote', 'Author'])

url = requests.get('https://quotes.toscrape.com/')

soup = BeautifulSoup(url.text, 'html.parser')

quotes = soup.findAll('span', attrs={'class':'text'})

authors = soup.findAll('small', attrs={'class':'author'})

for quote, author in zip(quotes, authors):
    author_text = author.text if author else 'Unknown Author'
    print(quote.text + " - " + author_text)
    writer.writerow([quote.text, author_text])
file.close()