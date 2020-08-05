from bs4 import BeautifulSoup
import requests,re

url='https://egypt.souq.com/eg-en/'
urls =[]
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
for link in soup.findAll('a',attrs={'href':re.compile(r'\w+')}):
    urls.append(link.get('href'))