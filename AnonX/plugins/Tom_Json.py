import asyncio
import config
from pyrogram import Client, filters
from pyrogram import filters
from strings import get_command
from strings.filters import command
from AnonX import app
from config import OWNER_ID
from AnonX.misc import SUDOERS
from pyrogram.types import 
DEVELOPERS = [5089553588]
OWNER_BOT = 5089553588

def load_tom_basic_devs():
    try:
        with open('tom_basic_devs.json', 'r') as file:
            tom_basic_devs = json.load(file)
    except FileNotFoundError:
        tom_basic_devs = {'basic_devs': {}}
    return tom_basic_devs

def dump_tom_basic_devs(tom_basic_devs):
    with open('tom_basic_devs.json', 'w') as file:
        json.dump(tom_basic_devs, file)

def load_tom_devs():
    try:
        with open('tom_devs.json', 'r') as file:
            tom_devs = json.load(file)
    except FileNotFoundError:
        tom_devs = {'devs': {}}
    return tom_devs

def dump_tom_devs(tom_devs):
    with open('tom_devs.json', 'w') as file:
        json.dump(tom_devs, file)

def load_tom_basic_creators():
    try:
        with open('tom_basic_creators.json', 'r') as file:
            tom_basic_creators = json.load(file)
    except FileNotFoundError:
        tom_basic_creators = {'basic_creators': {}}
    return tom_basic_creators

def dump_tom_basic_creators(tom_basic_creators):
    with open('tom_basic_creators.json', 'w') as file:
        json.dump(tom_basic_creators, file)

def is_basic_creator(_, __, message):
    tom_basic_creators = load_tom_basic_creators()
    user_id = str(message.from_user.id)
    return user_id in tom_basic_creators['basic_creators']



def load_tom_owners():
    try:
        with open('tom_owners.json', 'r') as file:
            tom_owners = json.load(file)
    except FileNotFoundError:
        tom_owners = {'owners': {}}
    return tom_owners


def dump_tom_owners(tom_owners):
    with open('tom_owners.json', 'w') as file:
        json.dump(tom_owners, file)


def load_tom_creators():
    try:
        with open('tom_creators.json', 'r') as file:
            tom_creators = json.load(file)
    except FileNotFoundError:
        tom_creators = {'creators': {}}
    return tom_creators


def dump_tom_creators(tom_creators):
    with open('tom_creators.json', 'w') as file:
        json.dump(tom_creators, file)

def creator(_, __, message):
    tom_creators = load_tom_creators()
    chat_id = str(message.chat.id)
    user_id = str(message.from_user.id)
    return chat_id in tom_creators['creators'] and user_id in tom_creators['creators'][chat_id]['creator_id']



def load_tom_admin():
    try:
        with open('tom_admin.json', 'r') as file:
            tom_admin = json.load(file)
    except FileNotFoundError:
        tom_admin = {'admin': {}}
    return tom_admin


def dump_tom_admin(tom_admin):
    with open('tom_admin.json', 'w') as file:
        json.dump(tom_admin, file)

def admin(_, __, message):
    tom_admin = load_tom_admin()
    chat_id = str(message.chat.id)
    user_id = str(message.from_user.id)
    return chat_id in tom_admin['admin'] and user_id in tom_admin['admin'][chat_id]['admin_id']


def load_tom_distinct():
    try:
        with open('tom_distinct.json', 'r') as file:
            tom_distinct = json.load(file)
    except FileNotFoundError:
        tom_distinct = {'admin': {}}
    return tom_distinct


def dump_tom_distinct(tom_distinct):
    with open('tom_distinct.json', 'w') as file:
        json.dump(tom_distinct, file)



def load_ban_mute_tom():
    try:
        with open('ban_mute_all_tom.json', 'r') as file:
            tom_all = json.load(file)
    except FileNotFoundError:
        tom_all = {}
    return tom_all


def save_ban_mute_tom(tom_all):
    with open('ban_mute_all_tom.json', 'w') as file:
        json.dump(tom_all, file)




def load_tom_mute_data():
    try:
        with open('tom_muted_users.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data


def save_tom_mute_data(data):
    with open('tom_muted_users.json', 'w') as file:
        json.dump(data, file)




#############               #####                         ###                      ###
      ###                   ##         ##                     ###  ##             ##  ###
      ###                 ##             ##                   ###    ##         ##    ###
      ###               ##                 ##                 ###      ##     ##      ###
      ###                 ##             ##                   ###        ####         ###
      ###                   ##        ##                      ###                       ###
      ###                      #####                          ###                      ###

def basic_dev(_, __, message):
    tom_basic_devs = load_tom_basic_devs()
    user_id = str(message.from_user.id)
    return user_id in tom_basic_devs['basic_devs']



def dev(_, __, message):
    tom_devs = load_tom_devs()
    user_id = str(message.from_user.id)
    return user_id in tom_devs['devs']


def is_basic_creator(_, __, message):
    tom_basic_creators = load_tom_basic_creators()
    user_id = str(message.from_user.id)
    return user_id in tom_basic_creators['basic_creators']


def owner(_, __, message):
    tom_owners = load_tom_owners()
    chat_id = str(message.chat.id)
    user_id = str(message.from_user.id)
    return chat_id in tom_owners['owners'] and user_id in tom_owners['owners'][chat_id]['owner_id']



def creator(_, __, message):
    tom_creators = load_tom_creators()
    chat_id = str(message.chat.id)
    user_id = str(message.from_user.id)
    return chat_id in tom_creators['creators'] and user_id in tom_creators['creators'][chat_id]['creator_id']



def admin(_, __, message):
    tom_admin = load_tom_admin()
    chat_id = str(message.chat.id)
    user_id = str(message.from_user.id)
    return chat_id in tom_admin['admin'] and user_id in tom_admin['admin'][chat_id]['admin_id']

def distinct(_, __, message):
    tom_distinct = load_tom_distinct()
    chat_id = str(message.chat.id)
    user_id = str(message.from_user.id)
    return chat_id in tom_distinct['admin'] and user_id in tom_distinct['admin'][chat_id]['admin_id']




#############               #####                         ###                      ###
      ###                   ##         ##                     ###  ##             ##  ###
      ###                 ##             ##                   ###    ##         ##    ###
      ###               ##                 ##                 ###      ##     ##      ###
      ###                 ##             ##                   ###        ####         ###
      ###                   ##        ##                      ###                       ###
      ###                      #####                          ###                      ###


def OWNER_ID_TOM(user_id, __, message):
	return user_id == OWNER_BOT



def PROGRAMMER_TOM(user_id, __, message):
	return user_id in DEVELOPERS




def basic_dev_tom(user_id, __, message):
    tom_basic_devs = load_tom_basic_devs()
    user_id = str(message.from_user.id)
    return user_id in tom_basic_devs['basic_devs']



def dev_tom(user_id, __, message):
    tom_devs = load_tom_devs()
    user_id = str(message.from_user.id)
    return user_id in tom_devs['devs']


def is_basic_creator_tom(user_id, __, message):
    tom_basic_creators = load_tom_basic_creators()
    user_id = str(message.from_user.id)
    return user_id in tom_basic_creators['basic_creators']


def owner_tom(user_id, chat_id, message):
    tom_owners = load_tom_owners()
    chat_id = str(message.chat.id)
    user_id = str(message.from_user.id)
    return chat_id in tom_owners['owners'] and user_id in tom_owners['owners'][chat_id]['owner_id']



def creator_tom(user_id, chat_id, message):
    tom_creators = load_tom_creators()
    chat_id = str(message.chat.id)
    user_id = str(message.from_user.id)
    return chat_id in tom_creators['creators'] and user_id in tom_creators['creators'][chat_id]['creator_id']



def admin_tom(user_id, chat_id, message):
    tom_admin = load_tom_admin()
    chat_id = str(message.chat.id)
    user_id = str(message.from_user.id)
    return chat_id in tom_admin['admin'] and user_id in tom_admin['admin'][chat_id]['admin_id']

def distinct_tom(user_id, chat_id, message):
    tom_distinct = load_tom_distinct()
    chat_id = str(message.chat.id)
    user_id = str(message.from_user.id)
    return chat_id in tom_distinct['admin'] and user_id in tom_distinct['admin'][chat_id]['admin_id']
















def DISTINCT(_, __, message):
	return filters.create(distinct)

def ADMIN(_, __, message):
	return filters.create(admin)


def CREATOR(_, __, message):
	return filters.create(creator)


def OWNER(_, __, message):
	return filters.create(owner)


def BASIC_CREATORS(_, __, message):
	return filters.create(is_basic_creator)


def DEVS(_, __, message):
	return filters.create(dev)


def SOUDERS(_, __, message):
	return filters.create(basic_dev)





def OWNER_ID(_, __, message):
	return message.from_user.id == OWNER_BOT



def TOM(_, __, message):
	return message.from_user.id in DEVELOPERS










tom_basic_devs = load_tom_basic_devs()
tom_devs = load_tom_devs()
tom_basic_creators = load_tom_basic_creators()
tom_owners = load_tom_owners()
tom_creators = load_tom_creators()
tom_admin = load_tom_admin()
tom_distinct = load_tom_distinct()
