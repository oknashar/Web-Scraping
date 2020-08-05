import requests
from bs4 import BeautifulSoup
from secrets import username,password
import urllib.request

payload={
    'email':username,
    'pass':password
}

POST_LOGIN_URL = 'https://mbasic.facebook.com/login'


with requests.Session() as session:
    post = session.post(POST_LOGIN_URL,data=payload)
    url = f'https://mbasic.facebook.com/ufi/reaction/profile/browser/fetch/?limit=150&shown_ids=100013991173981%2C100007265403023%2C100014091996552%2C100008831855434%2C100003008934289%2C100006992018323%2C100006013904199%2C100013798430186%2C100005152801383%2C100012669466548&total_count=41&ft_ent_identifier=771222086954594'

    page=session.get(url)
soup = BeautifulSoup(page.content, "html.parser")
names = soup.find_all('h3', class_='bk')
for name in names:
    print(name.text)
