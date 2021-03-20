from TwitterCrawler import Twitter
from RedditCrawler import RedditCrawler
from YahooCrawler import Yahoo

def main_crawl(searchString, limit):
    t = Twitter()
    t.set_Settings(searchString, limit)
    t.crawl()
    print("Twitter crawl complete - tweets.csv created!")

    y = Yahoo()
    y.set_Settings(searchString, limit)
    y.crawl()
    print("Yahoo news crawl complete -  yahoo.csv created!")

    r = RedditCrawler()
    r.set_Settings(searchString, limit)
    r.crawl()
    print("Reddit crawl complete -  reddit.csv created!")
    return None


main_crawl('tesla', 5)