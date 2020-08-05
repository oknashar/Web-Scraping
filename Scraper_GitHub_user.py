import requests
import re
import time
# import urllib.request offline
from bs4 import BeautifulSoup
# Set the URL you want to webscrape from
search=input('Enter your Search \n')
url = 'https://github.com/search?q={}&type=Users&p='.format(search)
data = {}
for page in range(10):
    r = requests.get(url + str(page))
    print(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    for link in soup.find_all('a',attrs={'class':'muted-link'}):
        print(link.get('href'))