
from bs4 import BeautifulSoup
import csv
import time
from urllib.request import urlopen

categories =("title", "score", "author", "r_platform", "o_platform", "publisher", "developer", "release_date", "rating")

my_data = []

file_contents = []

with open('GI_links_new.csv', 'r') as data:
    urls = csv.reader(data)
    for url in urls:
        file_contents.append(url)

with open('GIreview_new.csv', mode='a', newline='') as f:

    writer = csv.writer(f, delimiter=',')
    writer.writerow(categories)

    for url in file_contents:

        # could introduce some logic to skip to next row if 404 error

        time.sleep(4)
        print('Fetching link')
        page = urlopen(url[0]).read()
        soup = BeautifulSoup(page, "html.parser")

        try:
            title = soup.select("h1")[0].text.strip()
        except:
            title = "N/A"
        if soup("div", {"class": "review-summary-score"}):
            score = soup.findAll("div", {"class": "review-summary-score"})[0].text.strip()
        else:
            score = "N/A"
        if soup("a", {"class": "username"}):
            author = soup.findAll("a", {"class": "username"})[0].text.strip()
        else:
            author = "N/A"
        if soup("div", {"class": "game-details-reviewedon"}):
            r_platform = soup.findAll("div", {"class": "game-details-reviewedon"})[0].text.strip().replace("Reviewed on: ","")
        else:
            r_platform = "N/A"
        if soup("div", {"class": "game-details-platform"}):
            o_platform = soup.findAll("div", {"class": "game-details-platform"})[0].text.strip().replace("Also on:","").replace('\n\t\t\t','')
        else:
            o_platform = "N/A"
        if soup("div", {"class": "game-details-publisher"}):
            publisher = soup.findAll("div", {"class": "game-details-publisher"})[0].text.strip().replace("Publisher:","")
        else:
            publisher = "N/A"
        if soup("div", {"class": "game-details-developer"}):
            developer = soup.findAll("div", {"class": "game-details-developer"})[0].text.strip().replace("Developer:","")
        else:
            developer = "N/A"
        if soup("div", {"class": "game-details-release"}):
            release_date = soup.findAll("div", {"class": "game-details-release"})[0].text.strip().replace("Release:","")
        else:
            release_date = "N/A"
        if soup("div", {"class": "game-details-rating"}):
            rating = soup.findAll("div", {"class": "game-details-rating"})[0].text.strip().replace("Rating:", "")
        else:
            rating = "N/A"

        game_info = (title, score[0], author, r_platform, o_platform, publisher, developer, release_date, rating)

        my_data.append(game_info)

        data = game_info

        print(r_platform)
        print(o_platform)

        print('writing data')
        writer.writerow(data)