from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get('https://books.toscrape.com/index.html')
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

titles = soup.findAll('h3')
prices = soup.findAll('p', attrs={'class': 'price_color'})

for title in titles:
    print(title.text)

for price in prices:
    print(price.text)
