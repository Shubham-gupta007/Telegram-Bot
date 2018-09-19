from telegram.ext import Updater, MessageHandler, Filters

#polling new messages
updater = Updater(token= "671350989:AAGL5jf0iIDhgVltmWKVU2AvLqnMojwTtnE")

#new event handler
dispatcher = updater.dispatcher

def echo(bot, update):
    update.message.reply_text(update.message.text)

dispatcher.add_handler(MessageHandler(Filters.text, echo))

#start polling
updater.start_polling()
updater.idle()

"""

import telegram 
bot = telegram.Bot(token= "671350989:AAGL5jf0iIDhgVltmWKVU2AvLqnMojwTtnE")

for chats in bot.get_updates():
    print(chats.message.chat.first_name)


import requests
req = requests.get("https://api.telegram.org/bot671350989:AAGL5jf0iIDhgVltmWKVU2AvLqnMojwTtnE/getUpdates")

#print(req.json())

for chats in req.json()["result"]:
    print(chats["message"]["text"])

"""