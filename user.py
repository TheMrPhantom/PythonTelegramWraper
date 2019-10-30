import json

def saveUser(users):
    with open('user.json', 'w') as f:
        json.dump(users, f)

def loadUser():
    users={}
    with open('user.json') as json_file:
        users = json.load(json_file)
    return users

def modifyUser(users,chatID,data=None):
    users[str(chatID)]=data
    saveUser(users)

def addUser(users,chatID,data=None):
    users[str(chatID)]
    saveUser(users)

def removeUser(users,chatID):
    del users[str(chatID)]
    saveUser(users)

def getUser(users,chatID):
    return users[str(chatID)]