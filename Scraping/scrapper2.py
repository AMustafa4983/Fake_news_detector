import requests
from bs4 import BeautifulSoup
import pandas as pd

news = []
classifications = []

for j in range(1,1700):
    request = requests.get(f'https://www.politifact.com/search/factcheck/?page={j}&q=climate+change')

    soup = BeautifulSoup(request.content,'html5lib')

    titles = soup.find_all('div',{'class':'c-textgroup__title'})
    imgs = soup.find_all('img',{'class':'c-image__original'})

    for i in range(0,len(imgs)):
        new = titles[i].text.strip()
        classification = imgs[i]['src'].strip()
        if new not in news:
            news.append(new)
            classifications.append(classification)
            print(f'News: {new}')
    
df = pd.DataFrame({'news':news,'class':classifications})

df.to_csv('politicfact.csv')