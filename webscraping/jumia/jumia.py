from bs4 import BeautifulSoup
import requests
import pandas as pd

columns = {'name':[], 'price':[], 'img':[]}

url = 'https://www.jumia.ma/smartphones/?page='

for page in range(1,15):
    r = requests.get(url + str(page))
    soup = BeautifulSoup(r.content, 'html.parser')

    ancher = soup.find('div',{'class':'-paxs row _no-g _4cl-3cm-shs'})
    ancher = ancher.find_all('article',{'class':'prd _fb col c-prd'})

    for article in ancher: 
        img = article.find('a').find('div',{'class':'img-c'}).find('img',{'class','img'})
        name = article.find('a').find('div',{'class':'info'}).find('h3',{'class','name'})
        price = article.find('a').find('div',{'class':'info'}).find('div',{'class','prc'})
    
        columns['img'].append(img.get('data-src'))
        columns['name'].append(name.text)
        columns['price'].append(price.text)


pd.DataFrame(columns).to_csv('jumia/jumia.csv')   