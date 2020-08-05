from bs4 import BeautifulSoup
import re
import requests

all_site = [
    "https://enghamzasalem.com/",
    "https://www.ionixxtech.com/",
    "https://sumatosoft.com",
    "https://4irelabs.com/",
    "https://www.leewayhertz.com/",
    "https://stackoverflow.com",
    "https://www.vardot.com/en",
    "http://www.clickjordan.net/",
    "https://vtechbd.com/"

]
emails = []
tel = []
for site in all_site:
    req = requests.get(site)
    soup = BeautifulSoup(req.content, 'html.parser')
    for link in soup.find_all('a', attrs={'href': re.compile('mailto:')}):
        emails.append(link.get('href'))
    for link in soup.find_all('a', attrs={'href': re.compile('tel:')}):
        tel.append(link.get('href'))

print(emails)
print(tel)
