from TwitterCrawler import Twitter
from RedditCrawler import RedditCrawler
from YahooCrawler import Yahoo
from BotAPI import BotAPI
from Sentimental_Analysis import Sentimental_Analysis
from Web import generateWeb
import os


class CrawlerMain:

    def main_crawl(self, searchString, limit):
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

    def crawl_Twitter(self, limit):
        try:

            foodPanda = Twitter()
            foodPanda.set_Settings("FoodPanda", limit)
            foodPanda.crawl()
            print("FoodPanda Twitter crawl complete - tweets.csv created!")

            grabFood = Twitter()
            grabFood.set_Settings("GrabFood", limit)
            grabFood.crawl()
            print("GrabFood Twitter crawl complete - tweets.csv created!")

            deliveroo = Twitter()
            deliveroo.set_Settings("Deliveroo", limit)
            deliveroo.crawl()
            print("Deliveroo Twitter crawl complete - tweets.csv created!")
            return True, "Twitter crawl for all 3 delivery platform complete!"
        except:
            return False, "Twitter Crawling failed"

    def crawl_Yahoo(self, limit):
        try:
            foodPanda = Yahoo()
            foodPanda.set_Settings("FoodPanda", limit)
            foodPanda.crawl()
            print("FoodPanda Yahoo news crawl complete -  yahoo.csv created!")

            grabFood = Yahoo()
            grabFood.set_Settings("GrabFood", limit)
            grabFood.crawl()
            print("GrabFood Yahoo news crawl complete -  yahoo.csv created!")

            deliveroo = Yahoo()
            deliveroo.set_Settings("Deliveroo", limit)
            deliveroo.crawl()
            print("Deliveroo Yahoo news crawl complete -  yahoo.csv created!")
            return True, "Yahoo crawl for all 3 delivery platform complete!"
        except:
            return False, "Yahoo Crawling Failed"

    def crawl_Reddit(self, limit):
        try:
            foodPanda = RedditCrawler()
            foodPanda.set_Settings("FoodPanda", limit)
            foodPanda.crawl()
            print("FoodPanda reddit crawl complete -  reddit.csv created!")

            grabFood = RedditCrawler()
            grabFood.set_Settings("GrabFood", limit)
            grabFood.crawl()
            print("GrabFood reddit crawl complete -  reddit.csv created!")

            deliveroo = RedditCrawler()
            deliveroo.set_Settings("Deliveroo", limit)
            deliveroo.crawl()
            print("Deliveroo reddit crawl complete -  reddit.csv created!")
            return True, "Reddit crawl for all 3 delivery platform complete!"

        except:
            return False, "Reddit Crawling Failed"

    def sent_anal(self):
        try:
            sent = Sentimental_Analysis()
            sent.plot_radar()
            sent.plot_line()
            return True, "Sentimental Analysis Complete!"
        except:
            return False, "Failed to perform Aentimental Analysis"

    def generateWebpage(self):
        try:

            make = generateWeb()
            make.makeHTML()
            make.close()
            return True, "Webpage generated"
        except:
            return False, "Fail to generate webpage"

    def readcsv(self):
        read = BotAPI()
        try:
            read.readCsv('GrabFood', 'Twitter')
            read.readCsv('FoodPanda', 'Twitter')
            read.readCsv('Deliveroo', 'Twitter')

            read.readCsv('GrabFood', 'Reddit')
            read.readCsv('FoodPanda', 'Reddit')
            read.readCsv('Deliveroo', 'Reddit')

            read.readCsv('GrabFood', 'Instagram')
            read.readCsv('FoodPanda', 'Instagram')
            read.readCsv('Deliveroo', 'Instagram')

            read.readCsv('GrabFood', 'Yahoo')
            read.readCsv('FoodPanda', 'Yahoo')
            read.readCsv('Deliveroo', 'Yahoo')
            return('CSV read!')
        except:
            return('Unable to read CSV!')

    def dingding(self):
        '''! Ping
        @brief ping command allows the bot to ping a specific user within the telegram chat group'''
        try:
            os.system("git add -A")
            os.system('git commit -m "Build Github Pages"')
            os.system("git push origin Build-1.0")
            return('https://yeongzhenhong.github.io/oop/')
        except:
            return False
