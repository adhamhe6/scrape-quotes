# scraping_logins_selenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
import getpass

# browser_driver = Service('/path/to/chromedriver')
# url = webdriver.Chrome(service=browser_driver)
url = webdriver.Chrome(ChromeDriverManager().install())
url.get("https://quotes.toscrape.com")

url.find_element(By.LINK_TEXT, "Login").click()
time.sleep(3)

username = url.find_element(By.ID, "username")
password = url.find_element(By.ID, "password")
username.send_keys("admin")
my_pass = getpass.getpass()
password.send_keys(my_pass)

url.find_element(By.CSS_SELECTOR, "input.btn-primary").click()

quotes = url.find_elements(By.CLASS_NAME, "text")
authors = url.find_elements(By.CLASS_NAME, "author")

file = open("csv/scraped_quotes2.csv", "w", encoding='utf-8')
writer = csv.writer(file)

writer.writerow(["QUOTES", "AUTHORS"])

for quote, author in zip(quotes, authors):
    author_text = author.text if author else 'Unknown Author'
    print(quote.text + " - " + author_text)
    writer.writerow([quote.text, author_text])
file.close()