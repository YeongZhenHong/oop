import re
import csv
from time import sleep
from bs4 import BeautifulSoup
import requests
from Crawler import Crawler

"""! Headers dictionary
@brief Headers template for requesting a html.
"""
headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.google.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44'
}


"""! Yahoo class
@brief Allows an instance of the Yahoo class to be created, taking in user-input for search objective.
@brief Contains get_article function, to retrieve required informational fields from an article.
@brief Contains get_news function, to conduct searching of keyword and output of a csv file of all the articles.
"""
class Yahoo(Crawler):

    """! Yahoo initializer
    @brief takes in user-input keyword and initializes an instance of the Yahoo class.
    """

    def __init__(self):
        super().__init__()
        self.news_articles = []

    def set_Settings(self, searchString):
        super().set_searchString(searchString)

    """! Get article function
    @brief 
    """
    def get_article(self, stuff):
        title = stuff.find('h4', 's-title').text
        source = stuff.find('span', 's-source').text
        date = stuff.find('span', 's-time').text.replace('-','').strip()
        desc = stuff.find('p', 's-desc').text.strip()
        raw_link = stuff.find('a').get('href')
        unquote_link = requests.utils.unquote(raw_link)
        regex_pattern = re.compile(r'RU=(.+)\/RK')
        cleaned_link = re.search(regex_pattern, unquote_link).group(1)

        article = (title, source, date, desc, cleaned_link)
        return article


    def crawl(self):
        template = 'https://sg.news.search.yahoo.com/search?p={}'
        url = template.format(self.get_searchString())
        links = set()

        while True:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            stuffs = soup.find_all('div', 'NewsArticle')

            for stuff in stuffs:
                article = self.get_article(stuff)
                link = article[-1]
                if link not in links:
                    links.add(link)
                    self.news_articles.append(article)

            try:
                url = soup.find('a', 'next').get('href')
                sleep(1)
            except AttributeError:
                break

        with open('results.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Title', 'Source', 'Date', 'Description', 'Link'])
            writer.writerows(self.news_articles)
        return self.news_articles

y = Yahoo()
y.set_searchString('foodpanda')
y.crawl()

