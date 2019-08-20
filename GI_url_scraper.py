import requests
import re
import lxml
from bs4 import BeautifulSoup

# https://www.gameinformer.com/reviews?page=4

# loop through desired number of pages

url = 'https://www.gameinformer.com/reviews?page='
pages = (1, 2, 3, 4)
urls = ()

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

for page in pages:

    soup = BeautifulSoup(requests.get(url + str(pages)).content, 'lxml')

    #print(soup.find_all("a", href=True))
    #links = soup.find_all("a", class_="", href=re.compile("review"))
    #urls = soup.attrs['href']
    #print(urls)

    for link in soup.find_all('a', href=True, string=re.compile('Review')):
        #links = (link.get('href'))
        links = link['href']
        #urls = link.replace('reviews','')
        #print(links)
        filter_keys = {'reviews':'', 'legacy':''}
        #print(links)
        filtered = 'https://www.gameinformer.com' + replace_all(links, filter_keys)
        print(filtered)

#for page in pages:

#    requests.get(url +  pages)

# open url links for reviews on the pages

# get soup/desired page data