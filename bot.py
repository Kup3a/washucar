import telegram
from telegram.ext import Updater, CommandHandler

import settings


bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)
updater = Updater(token=settings.TELEGRAM_TOKEN)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)
