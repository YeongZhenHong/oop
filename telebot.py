# imports!
import telegram

from telegram.ext import Updater
from telegram.ext import CommandHandler
import auth_token

import mysql.connector
cnx = mysql.connector.connect(user='root',
                              host='127.0.0.1',
                              database='test')
cursor = cnx.cursor()


'''
@insertData(first_name,last_name,course)
dummy insert statement into local database for student object
the following insert statement would need to cater to the data that is fetch from the twtitter bot

'''
def insertData(first_name, last_name, course):

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
def selectAll():
    query = ("SELECT * FROM test.student")
    cursor.execute(query)
    astr = ''
    for i in cursor:
        astr += str(i)
    return astr


'''Updater'''
updater = Updater(
    token=auth_token.TOFU_CRAWLER_KEY, use_context=True)
dispatcher = updater.dispatcher

'''start functions'''

''' All functions would named with their command name  that is given
such as start/ fetch/insert commands that is available within telegram'''
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="@lianzniz hello! ")


def fetch(update, context):
    bstr = selectAll()
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=bstr)


def insert(update, context):
    # user_text = " ".join(context.args)
    try:
        insertData(context.args[0], context.args[1], context.args[2])
        context.bot.send_message(
        chat_id=update.effective_chat.id, text="Data inserted! ")
    except:
        context.bot.send_message(
        chat_id=update.effective_chat.id, text="invalid parameters! ")

    # update.message.reply_text("into what? " + user_text)
    # update.message.reply_text("what is this? " + context.args[0])
    # context.bot.send_message(
    #     chat_id=update.effective_chat.id, text="Data inserted! ")


''' ping command allows the bot to ping a specific user within the telegram chat group'''
def ping(update, context):
    for i in range(5):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="@lianzniz hello! ")


'''Command handlers'''
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
fetch_handler = CommandHandler('fetch', fetch)
dispatcher.add_handler(fetch_handler)
dispatcher.add_handler(CommandHandler('insert', insert))
dispatcher.add_handler(CommandHandler('ping', ping))

'''start the bot by calling this command'''
updater.start_polling()

# updater.stop()

# cursor.close()
# cnx.close()
