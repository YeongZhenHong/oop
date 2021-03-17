"""!
@file TelegramBot.py
@author Yeong Zhen Hong 2609703Y
@brief This file contains the TelegramBot class
@version 1.0
@section DESCRIPTION
Runs the Telegram to allow user to interact with the bot
"""

import telegram

from telegram.ext import Updater
from telegram.ext import CommandHandler
import auth_token
import time

import mysql.connector
from BotAPI import BotAPI
from TwitterBot import Analyze


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
            token=auth_token.TOFU_CRAWLER_KEY, use_context=True)
        TelegramBot.dispatcher = TelegramBot.updater.dispatcher
        self.initDB = BotAPI()

    def crawlTwitter(self, update, context):
        """! Function
        @brief getTweets gets an instance of Twitter Crawler to fetch tweets from Twitter's API
        @param self aaa
        @param update aaa
        @param context aaaaa
        @exception context.bot.send_message Fail to reply user with output
        """
        try:
            getTweets = Analyze(context.args[0]).initTwitter()
            time.sleep(5)
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="tweet output for " +
                context.args[0]
            )
            context.bot.sendDocument(
                chat_id=update.effective_chat.id, document=open("./tweets.csv", "rb"))
            context.bot.sendDocument(
                chat_id=update.effective_chat.id, document=open("./sent_anal.png", "rb"))
        except:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Failed to fetch new file!")

    def fetchTweets(self, update, context):
        """! fetchTweets(self,update,context)
        @brief fetches tweets from TwitterBot.py 
        @param self
        @param update
        @param context Fetches all the tweets from the database
        @param tweetsArray contains all the tweets that is called from the database
        """
        self.initDB.openCnx()
        tweetsArray = self.initDB.selectTweets()
        for item in tweetsArray:

            context.bot.send_message(
                chat_id=update.effective_chat.id, text=str(item))
        self.initDB.closeCnx()
    def startBot(self):
        """! Function
        @brief startsBot() start the bot by injecting handler and begin polling"""
        self.injectHandlers()
        self.updater.start_polling()
    

    def ping(self, update, context):
        '''! Function
        @brief ping command allows the bot to ping a specific user within the telegram chat group'''
        astr = ""
        for i in range(5):
            astr += context.args[0]+" hello! \n"
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=astr)
    

    def injectHandlers(self):
        """! injectHandlers(self)
        @brief Inject Command handlers
        add handlers into dispatcher to allow the bot to capture user input
        which would trigger function calls from within TelegramBot class
        """
        self.dispatcher.add_handler(
            CommandHandler('FetchTweets', self.fetchTweets))
        self.dispatcher.add_handler(CommandHandler('ping', self.ping))
        self.dispatcher.add_handler(CommandHandler(
            'CrawlTwitter', self.crawlTwitter))

    def killBot(self):
        """! Function
        @brief kills bot using updater.stop()"""
        self.updater.stop()

if __name__ == "__main__":
    aBot = TelegramBot()
    aBot.startBot()
