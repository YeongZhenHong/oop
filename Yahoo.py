import re
import csv
from time import sleep
from bs4 import BeautifulSoup
import requests

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.google.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44'
}


def get_article(stuff):
    title = stuff.find('h4', 's-title').text
    source = stuff.find('span', 's-source').text
    date = stuff.find('span', 's-time').text.replace('-','').strip()
    desc = stuff.find('p', 's-desc').text.strip()
    raw_link = stuff.find('a').get('href')
    unquote_link = requests.utils.unquote(raw_link)
    regex_pattern = re.compile(r'RU=(.+)\/RK')
    cleaned_link = re.search(regex_pattern, unquote_link).group(1)

    news_article = (title, source, date, desc, cleaned_link)
    return news_article


def get_news(search):
    template = 'https://sg.news.search.yahoo.com/search?p={}'
    url = template.format(search)
    news_articles = []
    links = set()

    while True:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        stuffs = soup.find_all('div', 'NewsArticle')
        print(stuffs)

        for stuff in stuffs:
            article = get_article(stuff)
            link = article[-1]
            if link not in links:
                links.add(link)
                news_articles.append(article)

        try:
            url = soup.find('a', 'next').get('href')
            sleep(1)
        except AttributeError:
            break

    with open('results.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Source', 'Date', 'Description', 'Link'])
        writer.writerows(news_articles)
    return news_articles


if __name__ == '__main__':
    articles = get_news('foodpanda')





