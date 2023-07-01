import requests
from bs4 import BeautifulSoup
import pandas as pd

titles = []
news = []
classifications = []
reviews = []

for j in range(1,17):
    request = requests.get(f'https://www.politifact.com/search/factcheck/?page=4&q=climate+change')

    soup = BeautifulSoup(request.content,'html5lib')

    attrs = soup.find_all('a',{'class':'strong'})
    for attr in attrs:
        req = requests.get(attr['href'])
        soup = BeautifulSoup(req.content,'html5lib')
        title = soup.find('h1',{'class':'entry-title'}).text
        new = soup.find('div',{'class':'claimshort'}).text
        classification = soup.find('img',{'class':'fact-check-card__row__verdict__img'})['src']
        review = soup.find('blockquote').text

        print(f'News: {new}, reivew: {review}')

        if new not in news:
            titles.append(title)
            news.append(new)
            classifications.append(classification)
            reviews.append(review)

df = pd.DataFrame({'title':titles,'news':news,'class':classifications,'review':reviews})

df.to_csv('climatefeedback.csv')