from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import CallbackQueryHandler
from telegram.ext import Filters
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import utils

import copy
import PythonTelegramWraper.botBackend as botBackend


def chatID(update):
    '''
    Get the chat id of an update object
    '''
    return update.effective_chat.id

#Specify command without slash e.g. "start"
def addBotCommand(command, function):
    '''
    Normal Telegram command,
    e.g command = "subscribe" then this method will be called when someone types: "/subscribe"
    '''
    handle = CommandHandler(command, function)
    botBackend.dispatcher.add_handler(handle)

#Filter param is e.g. Filters.photo
def addBotMessage(filter, function):
    '''
    Filter param is e.g. Filters.photo
    '''
    handle = MessageHandler(filter, function)
    botBackend.dispatcher.add_handler(handle)


def startBot():
    '''
    Starts the bot
    '''
    botBackend.updater.start_polling()

def save():
    '''
    Stores the user data in the user.json
    '''
    botBackend.user.saveUser(botBackend.users)


def modifyUser(chatID,data=None):
    '''
    Changes the data of a user to the supplied data, creates user if not existing
    '''
    botBackend.user.modifyUser(botBackend.users,chatID,data)


def user(chatID):
    '''
    Gets the data of a user (None if not existing)
    '''
    return botBackend.user.getUser(botBackend.users,chatID)

def removeUser(chatID):
    '''
    Removes a user
    '''
    botBackend.user.removeUser(botBackend.users,chatID)

def sendMessage(chatID, message,isHTML=False,rpl_markup=None):
    
    if not isHTML:
        botBackend.updater.bot.sendMessage(int(chatID), 
                    message, 
                    parse_mode="Markdown",reply_markup=rpl_markup)
    else:
        botBackend.updater.bot.sendMessage(int(chatID), 
                    message, 
                    parse_mode="HTML",reply_markup=rpl_markup)

def sendPhoto(chatID, src, captionText=None):
    botBackend.dispatcher.bot.send_photo(chat_id=chatID, photo=src,caption=captionText,parse_mode="Markdown")

#Return a copy of the user data
#!Can be huge!
def getUserData():
    return copy.deepcopy(botBackend.users)

def getUserDataOriginal():
    return botBackend.users

def getBot():
    return botBackend.updater.bot

def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu