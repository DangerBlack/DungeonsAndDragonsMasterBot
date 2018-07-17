#!/bin/python
# -*- coding: utf-8 -*-
# telebot is needed
# requests is needed
import telebot
import sys
import os
import getopt
#import js2py
#import subprocess
import runchar
from telebot import types
import csv
import random


CSV_NAME = 0
CSV_RARITY = 1
CSV_DESCRIPTION = 2

gItems = []

def printutf8(s, ofile=sys.stdout.buffer):
    outs = str(s) + "\n"
    ofile.write(outs.encode('utf-8'))
    ofile.flush()
           
logall = 0

try:
    optlist, args = getopt.getopt(sys.argv[1:], "sel", ["save", "except-save", "log-all"])
except getopt.GetOptError as err:
    print(str(err), file=sys.stderr)
    exit(1)

for o,v in optlist:
    if o in ("-s", "--save"):
        save = 1
    elif o in ("-e", "--except-save"):
        exceptsave = 1
    elif o in ("-l", "--log-all"):
        logall = 1
    else:
        assert False, "unhandled option (" + o + ")"

secret = ""
with open("./secret.txt", "r") as f:
    secret = f.readline().rstrip('\n')

with open('items/itemsL.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='#')
    for row in spamreader:
        gItems.append(row)

bot = telebot.TeleBot(secret)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello, I'm a bot!\nI can make random npc for your campain and more over!\nJust click on \n/npc\nfor a random NPC\nor try\n/npc 5\nfor a level 5 random NPC\n /item for a random magic item")



#============================NPC========================================
@bot.message_handler(commands=["npc",'spwan'])
def send_response(message):
    chat_id = message.chat.id
    bot.send_chat_action(chat_id, 'typing')
    level = message.text.split(" ")
    if(len(level)>1):
        level = level[1]
        if(not level.isdigit()):
            level = 0
        out = runchar.PyJsHoisted_run_(level,0)
        out = ''+str(out)[1:-1].replace("==EOF==",'\n')
        bot.send_message(chat_id, out, parse_mode="HTML")
    else:
        out = "Witch level?"
        msg = bot.send_message(chat_id, out, parse_mode="HTML")
        bot.register_next_step_handler(msg,process_level_step)
    
def process_level_step(message):
    try:
        chat_id = message.chat.id
        level = message.text
        printutf8("LEVEL: "+str(level), ofile=sys.stderr.buffer)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        itembtn1 = types.KeyboardButton('Male')
        itembtn2 = types.KeyboardButton('Female')
        markup.add(itembtn1, itembtn2)
        out = "Select gender?"
        msg = bot.send_message(chat_id, out, reply_markup=markup)
        bot.register_next_step_handler(msg,process_gender_step,level)
    except Exception as e:
        printutf8(e, ofile=sys.stderr.buffer)
        bot.reply_to(message, 'You are wrong')

def process_gender_step(message,level):
    try:
        chat_id = message.chat.id
        printutf8("LEVEL: "+str(level), ofile=sys.stderr.buffer)
        gender = 0
        printutf8("SEX: "+str(message.text), ofile=sys.stderr.buffer)
        if(message.text == 'Male'):
            gender = 1
        else:
            gender = 2        
        out = runchar.PyJsHoisted_run_(level,gender)
        out = ''+str(out)[1:-1].replace("==EOF==",'\n')
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(chat_id, out, parse_mode="HTML", reply_markup=markup)
    except Exception as e:
        printutf8(e, ofile=sys.stderr.buffer)
        bot.reply_to(message, 'You are wrong')

#=======================STOP NPC========================================
@bot.message_handler(commands=['item'])
def send_response(message):
    try:
        chat_id = message.chat.id
        item = random.choice(gItems)
        out = '<b>'+item[CSV_NAME]+"</b>\n"+item[CSV_RARITY]+"\n"+item[CSV_DESCRIPTION].replace("==EOF==",'\n')
        bot.send_message(chat_id, out, parse_mode="HTML")
    except Exception as e:
        chat_id = message.chat.id
        item = random.choice(gItems)
        out = '<b>'+item[CSV_NAME]+"</b>\n"+item[CSV_RARITY]+"\nSearch online: https://www.aidedd.org/dnd-filters/"
        bot.send_message(chat_id, out, parse_mode="HTML")
        printutf8(e, ofile=sys.stderr.buffer)
       

@bot.message_handler(commands=['test'])
def send_response(message):
    chat_id = message.chat.id
    out = 'test'
    bot.send_message(chat_id, out, parse_mode="HTML")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	out = "Command not found take a 🐧 instead!"
	bot.reply_to(message, out, parse_mode="HTML")

while(True):
    try:
        #bot.polling(none_stop = True, interval = 3)
        bot.infinity_polling(True)
    except Exception as e:
        print("[%s] error on bot polling" % (datetime.datetime.now()))
        printutf8(e, ofile=sys.stderr.buffer)
        time.sleep(30)
