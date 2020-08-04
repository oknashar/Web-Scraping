import csv,json,csv,time,requests
from bs4 import BeautifulSoup
import urllib.request

filecsv = open('souq.csv','w',encoding='utf-8')
filejson = open('souq.json','w',encoding='utf-8')

url = 'https://egypt.souq.com/eg-en/apple/s/?as=1&section=2&page='
filejson.write('[ \n')
data = {}
csv_column = ['name','price','img']

for page in range(5):
    print('___________page{}----------'.format(page))
    f=requests.get(url+str(page))
    print(url+str(page))
    soup = BeautifulSoup(f.content,'html.parser')
    ancher  =soup.find_all('div',{'class':'column column-block block-list-large single-item'})
    writer = csv.DictWriter(filecsv,fieldnames=csv_column)
    writer.writeheader()
    for pt in ancher:
        name = pt. find('h1',{'class':'itemTitle'})
        price = pt. find('h3',{'class':'itemPrice'})
        img = pt. find('img',{'class':'imageUrl'})
        print(name.text)
        print(price.text)
        print(img.get('src'))
        if img:
            writer.writerow({
                'name':name.text.replace('\t','').strip('\r\n'),
                'price':price.text,
                'img':img.get('src')
                })
            data['name']=name.text.replace('\t','').strip('\r\n')
            data['price']=price.text
            data['img']=img.get('src')
            json_data = json.dumps(data,ensure_ascii=False)
            filejson.write(json_data)
            filejson.write(',\n')

filejson.write('\n]')
filejson.close()
filecsv.close()
