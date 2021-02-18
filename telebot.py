# imports!
import telegram

from telegram.ext import Updater
from telegram.ext import CommandHandler
import mysql.connector
cnx = mysql.connector.connect(user='root',
                              host='127.0.0.1',
                              database='test')
cursor = cnx.cursor()


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


def selectAll():
    query = ("SELECT * FROM test.student")
    cursor.execute(query)
    astr = ''
    for i in cursor:
        astr += str(i)
    return astr


'''Updater'''
updater = Updater(
    token='1649238841:AAFbq0Npfxq8Hz5WdApE3JBrRILm87tZuD4', use_context=True)
dispatcher = updater.dispatcher

'''start functions'''


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


def ping(update, context):
    for i in range(20):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="@lianzniz hello! ")


'''Command handlers'''
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
fetch_handler = CommandHandler('fetch', fetch)
dispatcher.add_handler(fetch_handler)
dispatcher.add_handler(CommandHandler('insert', insert))
dispatcher.add_handler(CommandHandler('ping', ping))

updater.start_polling()


# updater.stop()

# cursor.close()
# cnx.close()
