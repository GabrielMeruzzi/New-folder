import re
import urllib.request
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Web_scraping'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all('a', href=True)

for link in links:
    href = link['href']
    if href.startswith('/wiki/'):
        print(href)