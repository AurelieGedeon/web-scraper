from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get('https://books.toscrape.com/index.html')
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

star_ratings = soup.findAll('p', attrs={'class': 'star-rating'})
