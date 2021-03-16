'''
Coded by Yeong Zhen Hong 2609703Y
'''

import telegram

from telegram.ext import Updater
from telegram.ext import CommandHandler
import auth_token
import time

import mysql.connector
from BotAPI import BotAPI
from TwitterBot import Analyze


class Telebot:
    '''Updater'''
    updater = Updater(
        token=auth_token.TOFU_CRAWLER_KEY, use_context=True)
    dispatcher = updater.dispatcher
    initDB = BotAPI()

    '''start functions'''

    ''' All functions would named with their command name  that is given
    such as start/ fetch/insert commands that is available within telegram'''

    def start(self, update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="@lianzniz hello! ")

    def fetch(self, update, context):
        bstr = self.initDB.selectAll()
        for item in bstr:
            
            context.bot.send_message(
            chat_id=update.effective_chat.id, text=str(item))

        # print(bstr)
        

    def insert(self, update, context):
        # user_text = " ".join(context.args)
        try:
            self.initDB.insertData(
                context.args[0], context.args[1], context.args[2])
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Data inserted! ")
        except:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="invalid parameters! ")

        # update.message.reply_text("into what? " + user_text)F
        # update.message.reply_text("what is this? " + context.args[0])
        # context.bot.send_message(
        #     chat_id=update.effective_chat.id, text="Data inserted! ")

    ''' ping command allows the bot to ping a specific user within the telegram chat group'''

    def ping(self, update, context):
        astr = ""
        for i in range(5):
            astr += "@lianzniz hello! \n"
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=astr)

    def reply(self, update, context):
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

    '''Command handlers'''

    def injectHandlers(self):
        '''Command Handlers
        used to detect user inputs with their commands        
        '''
        self.dispatcher.add_handler(CommandHandler('start', self.start))
        self.dispatcher.add_handler(CommandHandler('fetch', self.fetch))
        self.dispatcher.add_handler(CommandHandler('insert', self.insert))
        self.dispatcher.add_handler(CommandHandler('ping', self.ping))
        self.dispatcher.add_handler(CommandHandler('reply', self.reply))

    '''start the bot by calling this command'''

    def startBot(self):
        self.injectHandlers()
        self.updater.start_polling()

    # updater.stop()

    # cursor.close()
    # cnx.close()


if __name__ == "__main__":
    aBot = Telebot()
    aBot.startBot()
