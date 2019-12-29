from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import CallbackQueryHandler
from telegram.ext import Filters
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import utils

import PythonTelegramWraper.config as config
import PythonTelegramWraper.user as user

#Setting up the dispatcher in which the available
#bot messages will be stored
updater = Updater(token=config.telegramToken, use_context=True)
dispatcher = updater.dispatcher

#Setting up cache
users=user.loadUser()