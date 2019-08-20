import requests
import re
import csv
import pandas as pd
from bs4 import BeautifulSoup
import time

# loop through desired number of pages

url = 'https://www.gameinformer.com/reviews?page='

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

for page in range(4):

        time.sleep(7)
        print("Waiting to begin loop:")

        r = requests.get(url + str(page))
        soup = BeautifulSoup(r.content, "html.parser")
        print("Getting links:")
        for link in soup.find_all("a", string=re.compile('Review')):
            #print(link.get("href"))

            links = link['href']
            #print(links)
            filter_keys = {'reviews': '', 'legacy': ''}
            filtered = 'https://www.gameinformer.com' + replace_all(links, filter_keys)
            #print(filtered)

            with open('GI_links_new.csv', mode='a', newline='') as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerow([filtered])

        print("Loop finished")

string = ["https://www.gameinformer.com/"]

GI_urls = pd.read_csv('GI_links_new.csv')
GI_cleaned = GI_urls.drop_duplicates()
GI_cleaned = GI_cleaned[~GI_cleaned.isin(["https://www.gameinformer.com/"])]
GI_cleaned.to_csv('GI_cleaned_new.csv', encoding='utf-8', index=False)



