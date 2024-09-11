import re
import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/list/ls055592025/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

titulos = soup.findAll('h3', attrs={'class':'ipc-title__text'})

for i, title in enumerate(titulos[:5]):
    movie = title.text.strip()
    print(movie)

