# import telegram

# bot = telegram.Bot(token='1649238841:AAFbq0Npfxq8Hz5WdApE3JBrRILm87tZuD4')
# print(bot.get_me())
# import telegram

from telegram.ext import Updater
from telegram.ext import CommandHandler
'''Updater'''
updater = Updater(token='1649238841:AAFbq0Npfxq8Hz5WdApE3JBrRILm87tZuD4', use_context=True)
dispatcher = updater.dispatcher

'''start functions'''
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def fetch(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

'''Command handlers'''
start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)
fetch_handler = CommandHandler('fetch',fetch)
dispatcher.add_handler(fetch_handler)


updater.start_polling()


updater.stop()