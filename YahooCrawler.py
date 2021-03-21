import re
import csv
from time import sleep
from bs4 import BeautifulSoup
import requests
from Crawler import Crawler
import datetime

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


"""! Yahoo class inheriting Crawler class.
@brief Allows an instance of the Yahoo class to be created, taking in user-input for search objective.
@brief Contains get_article function, to retrieve required informational fields from an article.
@brief Contains get_news function, to conduct searching of keyword and output of a csv file of all the articles.
"""


class Yahoo(Crawler):

    """! Yahoo initializer
    @brief Creates an instance of class Yahoo to conduct crawling of news articles.
    """

    def __init__(self):
        super().__init__()
        self.news_articles = []

    """! set_Settings function
    @brief Sets a keyword to search for.
    """

    def set_Settings(self, searchString):
        super().set_searchString(searchString)
        super().set_searchLimit(limit)

    def get_article(self, thing):
        """! Get article function
        @param An article
        @brief Pulls out required information from the article and returns a tuple with the fields.
        """
        currentDate = datetime.datetime.now()

        title = thing.find('h4', 's-title').text
        source = thing.find('span', 's-source').text
        # Get the number of days ago from post date
        daysAgo = thing.find(
            'span', 's-time').text.replace('·', ' ').strip("days ago")
        # Check for the number of days to minus off
        minusDays = datetime.timedelta(int(daysAgo))
        desc = thing.find('p', 's-desc').text.strip()
        raw_link = thing.find('a').get('href')
        unquote_link = requests.utils.unquote(raw_link)
        regex_pattern = re.compile(r'RU=(.+)\/RK')
        cleaned_link = re.search(regex_pattern, unquote_link).group(1)
        # Minus off the number of days from current date
        date = (currentDate-minusDays).date()
        article = (title, source, date, desc, cleaned_link)
        return article

    """! crawl function
    @brief Html request into yahoo news + search word, finds all news article divisions and
    writes a output csv file from news_article array.
    """

    def crawl(self):
        template = 'https://sg.news.search.yahoo.com/search?p={}'
        url = template.format(self.get_searchString())
        links = set()
        limit = self.get_searchLimit()

        if limit <= 0:
            raise ValueError("Error, that is not a positive number!")
        while True:
            try:
                response = requests.get(url, headers=headers)
                soup = BeautifulSoup(response.text, 'html.parser')
                things = soup.find_all('div', 'NewsArticle')

                for thing in things:
                    article = self.get_article(thing)
                    link = article[-1]
                    if link not in links:
                        links.add(link)
                        self.news_articles.append(article)
                if(limit > 0):
                    limit -= 10
                    try:
                        url = soup.find('a', 'next').get('href')
                        sleep(1)
                    except AttributeError:
                        break
                else:
                    break
            except Exception as err:
                print(err)
                break

        with open('./CSV/'+self.get_searchString()+'_Yahoo.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Title', 'Source', 'Date', 'Description', 'Link'])
            writer.writerows(self.news_articles)
        return self.news_articles
