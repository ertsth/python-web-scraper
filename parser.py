import requests
from bs4 import BeautifulSoup

url='https://www.pravda.com.ua/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
headlines = soup.find_all('div', class_ = 'article_header')
for x in headlines:
    print(x.find('a').get('href'))
    print(x.find('a').text)
