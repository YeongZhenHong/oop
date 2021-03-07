# imports!
import telegram

from telegram.ext import Updater
from telegram.ext import CommandHandler
import auth_token

import mysql.connector

'''
Connections to mysql service
'''
cnx = mysql.connector.connect(user=auth_token.MYSQL_DBUSER,
                              host=auth_token.MYSQL_HOST,
                              database=auth_token.MYSQL_DBNAME)
cursor = cnx.cursor()


'''
@insertData(first_name,last_name,course)
dummy insert statement into local database for student object
the following insert statement would need to cater to the data that is fetch from the twtitter bot

'''


class TelegramBot:
    '''Updater'''
    updater = Updater(
    token=auth_token.TOFU_CRAWLER_KEY, use_context=True)
    dispatcher = updater.dispatcher

    def insertData(self, first_name, last_name, course):

        # first_name = input("Please input first name ")
        # last_name = input("Please input last name ")
        # course = input("Please input course ")
        try:
            add_student = ("INSERT INTO test.student " +
                           "(first_name, last_name, course) " +
                           "VALUES ('"+first_name+"', '"+last_name+"','"+course+"')")

            cursor.execute(add_student)
            cnx.commit()
            return True
        except:
            pass

    '''
    @selectAll() function to be changed to select all the data from within the database
    under the query table '''

    def selectAll(self):
        query = ("SELECT * FROM test.student")
        cursor.execute(query)
        astr = ''
        for i in cursor:
            astr += str(i)
        return astr

    '''start functions'''

    ''' All functions would named with their command name  that is given
    such as start/ fetch/insert commands that is available within telegram'''

    def start(self, update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="@lianzniz hello! ")

    def fetch(self, update, context):
        bstr = self.selectAll()
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=bstr)

    def insert(self, update, context):
        # user_text = " ".join(context.args)
        try:
            insertData(context.args[0], context.args[1], context.args[2])
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
        for i in range(5):
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="@lianzniz hello! ")

    '''Command handlers'''

    def injectHandlers(self):
       

        '''Command Handlers
        used to detect user inputs with their commands        
        '''
        self.dispatcher.add_handler(CommandHandler('start',self.start))
        self.dispatcher.add_handler(CommandHandler('fetch', self.fetch))
        self.dispatcher.add_handler(CommandHandler('insert', self.insert))
        self.dispatcher.add_handler(CommandHandler('ping', self.ping))

    '''start the bot by calling this command'''

    def startBot(self):
        self.injectHandlers()
        self.updater.start_polling()

    # updater.stop()

    # cursor.close()
    # cnx.close()


a = TelegramBot()

a.startBot()
