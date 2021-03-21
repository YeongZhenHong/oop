"""! 
@file TelegramBot.py
@author Yeong Zhen Hong 2609703Y
@brief This file contains the TelegramBot class
@version 1.0
@section DESCRIPTION
Runs the Telegram to allow user to interact with the bot
"""

import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler
import Auth_Token
import time
import os

import mysql.connector
from BotAPI import BotAPI
from TwitterCrawler import Twitter
from CrawlerProgram import CrawlerMain


class TelegramBot:
    """! TelegramBot class
    Defines a Telegram bot object to capture user input for TofuCrawlerBot
    to allow users to get the bot to crawl information to them before replying 
    with the crawled data
    """

    def __init__(self):
        """! TelegramBot class initializer
        @brief updater takes in Telegram's API key to be used for getting the bot to send a receive 
        updates from Telegram servers
        @brief dispatcher dispatches all the updates to its registered handlers
        @brief initDB creates an instances of BOTAPI() to allow the bot to perform API calls to 
        interact with the databases
        @return an instance of TelegramBot class initialized with the parameters
        """
        TelegramBot.updater = Updater(
            token=Auth_Token.TOFU_CRAWLER_KEY, use_context=True)
        TelegramBot.dispatcher = TelegramBot.updater.dispatcher
        self.initDB = BotAPI()
        self.crawlerMain = CrawlerMain()
        

    def start(self, update, context):
        """! Start Function
        @brief replies a brief explaination on how to use the bot
        """
        message = """
        TofuCrawler Bot!\n
        I can perform data crawling from Twitter,Reddit,Yahoo and Instagram\n
        /Crawl [platform] [data name] - Crawl data from a specific platform\n
        /Crawlall [data name] - Crawl data from all 4 platforms\n
        /CrawTwitter [data name] [number of tweets] - Crawl a specific number of tweets from twitter\n
        /ping @username - pings a user 5 times in the chat
        """
        # keyboard = [[
        #     InlineKeyboardButton("Crawl data", callback_data=self.crawl),
        #     InlineKeyboardButton("Ping someone", callback_data=self.ping),
        # ],
        #     [InlineKeyboardButton("Kill Bot", callback_data=self.killBot())], ]
        # reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)
        # update.message.reply_text('Please choose:', reply_markup=reply_markup)

    def crawlTwitter(self, update, context):
        """! Function
        @brief getTweets gets an instance of Twitter Crawler to fetch tweets from Twitter's API
        @exception context.bot.send_message Fail to reply user with output
        """
        try:
            getTweets = Twitter().set_Settings(
                context.args[0], context.args[1])
            # getTweets = Twitter(context.args[0]).crawl()
            time.sleep(10)
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="tweet output for " +
                context.args[0]
            )
            context.bot.sendDocument(
                chat_id=update.effective_chat.id, document=open("./pagination/testhome.html", "rb"))
            context.bot.sendDocument(
                chat_id=update.effective_chat.id, document=open("./sent_anal.png", "rb"))
        except:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Failed to crawl twitter!!")

    def crawl(self, update, context):
        """! Function
        @brief getTweets gets an instance of Twitter Crawler to fetch tweets from Twitter's API
        @param self aaa
        @param update aaa
        @param context aaaaa
        @exception context.bot.send_message Fail to reply user with output
        """
        limit = 10
        # limit = int(context.args[0])
        
        
        try:
            
            # context.bot.send_message(chat_id=update.effective_chat.id, text=self.crawlerMain.crawl_Twitter(limit)[1])
            # context.bot.send_message(chat_id=update.effective_chat.id, text=self.crawlerMain.crawl_Yahoo(limit)[1])
            # context.bot.send_message(chat_id=update.effective_chat.id, text=self.crawlerMain.crawl_Reddit(limit)[1])
            # context.bot.send_message(chat_id=update.effective_chat.id, text=self.crawlerMain.sent_anal())
            context.bot.send_message(chat_id=update.effective_chat.id, text=self.crawlerMain.generateWebpage()[1])
            time.sleep(15)


            # context.bot.sendDocument(chat_id=update.effective_chat.id, document=open("./CSV/FoodPanda_Twitter.csv", "rb"))
            # context.bot.sendDocument(chat_id=update.effective_chat.id, document=open("./CSV/Deliveroo_Twitter.csv", "rb"))
            # context.bot.sendDocument(chat_id=update.effective_chat.id, document=open("./CSV/GrabFood_Twitter.csv", "rb"))
            # context.bot.sendDocument(chat_id=update.effective_chat.id, document=open("./sent_anal_spider.png", "rb"))
            context.bot.sendDocument(chat_id=update.effective_chat.id, document=open("./docs/index.html", "rb"))
        except:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Failed to crawl twitter!!")

    def fetchTweets(self, update, context):
        """! fetchTweets(self,update,context)
        @brief fetches tweets from TwitterBot.py 
        @param self
        @param update
        @param context Fetches all the tweets from the database
        @param tweetsArray contains all the tweets that is called from the database
        """
        try:
            self.initDB.openCnx()
            tweetsArray = self.initDB.selectTweets()
            for item in tweetsArray:

                context.bot.send_message(
                    chat_id=update.effective_chat.id, text=str(item))
            self.initDB.closeCnx()
            return True
        except:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Failed to fetch tweets from database!")
            return False

    def startBot(self):
        """! Function
        @brief startsBot() start the bot by injecting handler and begin polling"""
        try:
            self.injectHandlers()
            self.updater.start_polling()
            return True
        except:
            print("Failed to start telegram bot! ")
            return False

    def killBot(self):
        """! kill bot
        @brief kills bot using updater.stop()"""
        try:
            self.updater.stop()
            return True
        except:
            return False

    def ping(self, update, context):
        '''! Ping
        @brief ping command allows the bot to ping a specific user within the telegram chat group'''
        try:
            os.system("git add ./docs/index.html")
            os.system('git commit -m "Build Github Pages"')
            os.system("git push origin hong")
            return True
        except:
            return False
        
    # def ping(self, update, context):
    #     '''! Ping
    #     @brief ping command allows the bot to ping a specific user within the telegram chat group'''
    #     astr = ""
    #     for i in range(5):
    #         astr += context.args[0]+" hello! \n"
    #     context.bot.send_message(
    #         chat_id=update.effective_chat.id, text=astr)

    def injectHandlers(self):
        """! injectHandlers(self)
        @brief Inject Command handlers
        add handlers into dispatcher to allow the bot to capture user input
        which would trigger function calls from within TelegramBot class
        """
        try:
            self.dispatcher.add_handler(
                CommandHandler('FetchTweets', self.fetchTweets))
            self.dispatcher.add_handler(CommandHandler('start', self.start))
            self.dispatcher.add_handler(CommandHandler('ping', self.ping))
            self.dispatcher.add_handler(CommandHandler('Crawl', self.crawl))
            self.dispatcher.add_handler(CommandHandler(
                'CrawlTwitter', self.crawlTwitter))
            return True
        except:
            print("Failed to inject handlers!")
            return False


if __name__ == "__main__":
    aBot = TelegramBot()
    aBot.startBot()
