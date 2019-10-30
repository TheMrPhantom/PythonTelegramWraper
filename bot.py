from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import CallbackQueryHandler
from telegram.ext import Filters
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import utils

import copy
import botBackend

#Get the chat id of an update object
def chatID(update):
    return update.effective_chat.id

#Specify command without slash e.g. "start"
def addBotCommand(command, function):
    handle = CommandHandler(command, function)
    botBackend.dispatcher.add_handler(handle)

#Filter is e.g. Filters.photo
def addBotMessage(filter, function):
    handle = CommandHandler(filter, function)
    botBackend.dispatcher.add_handler(handle)

#Starts the bot
def startBot():
    botBackend.updater.start_polling()

#Stores the user data in the user.json
def save():
    botBackend.user.saveUser(botBackend.users)

#Changes the data of a user to the applied data
def modifyUser(chatID,data=None):
    botBackend.user.modifyUser(botBackend.users,chatID,data)

#Adds a user optional with data
def addUser(chatID,data=None):
    botBackend.user.addUser(botBackend.users,chatID,data)

#Removes a user
def removeUser(chatID):
    botBackend.user.removeUser(botBackend.users,chatID)

#Return a copy of the user data
#!Can be huge!
def getUserData():
    return copy.deepcopy(botBackend.users)