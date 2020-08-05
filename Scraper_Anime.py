from bs4 import BeautifulSoup
import re,requests

sites =[
    'https://anime-4u.com/',
]
all_pages =[]
linkes=[]
for site in sites:
    req = requests.get(site)
    soup=BeautifulSoup(req.content,'html.parser')
    for link in soup.find_all('a',attrs={'href':re.compile('^https:')}):
        all_pages.append(link.get('href'))
print(all_pages)
for page in all_pages:
    req = requests.get(page)
    soup=BeautifulSoup(req.content,'html.parser')
    for link in soup.find_all('iframe',attrs={}):
        linkes.append(link.get('src'))
print(linkes)
