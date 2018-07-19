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
import city


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
    bot.reply_to(message, "Hello, I'm a bot!\nI can make random npc for your campain and more over!\nJust click on \n/npc\n<i>for a random NPC</i>\n/npc 5\n<i>for a level 5 random NPC</i>\n/item\n<i>for a random magic item</i>\n/map\n<i>for a random map</i>", parse_mode="HTML")



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
#===========================ITEM========================================
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
       
#====================STOP===ITEM========================================
#===========================MAP=========================================
@bot.message_handler(commands=['map','city','village','town'])
def send_response(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(row_width=1,one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('Small')
    #8
    itembtn2 = types.KeyboardButton('Medium')
    #18
    itembtn3 = types.KeyboardButton('Large')
    #43
    markup.add(itembtn1, itembtn2,itembtn3)
    out = "Select map Size?"
    msg = bot.send_message(chat_id, out, reply_markup=markup)
    bot.register_next_step_handler(msg,process_map_size_step)

def getSizeByName(name):
    if name == 'Small':
        return random.choice([2,4,6,8,10,12])
    if name == 'Medium':
        return random.choice([12,14,16,18,20,22.23,24])
    if name == 'Large':
        return random.choice([24,26,28,30,32.36,38,40,42,44,46,48])
    return random.choice([8,18,43])
def process_map_size_step(message):
    try:
        chat_id = message.chat.id
        size = getSizeByName(message.text)
        printutf8("MAP SIZE: "+str(size), ofile=sys.stderr.buffer)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        itembtn1 = types.KeyboardButton('No - Random detail')
        itembtn2 = types.KeyboardButton('Yes - Pick detail')
        markup.add(itembtn1, itembtn2)
        out = "Do you want to define detail?"
        msg = bot.send_message(chat_id, out, reply_markup=markup)
        bot.register_next_step_handler(msg,process_map_detail_step,size)
    except Exception as e:
        printutf8(e, ofile=sys.stderr.buffer)
        bot.reply_to(message, 'You are wrong')
        

MAP_STEP = ["Citadel","Plaza","Temple","Walls","Shanty town","River","Coast"]
        
def process_map_detail_step(message,size):
    try:
        chat_id = message.chat.id
        detail = message.text
        printutf8("MAP Detail: "+str(detail), ofile=sys.stderr.buffer)
        if(message.text == 'No - Random detail'):
            out = "http://fantasycities.watabou.ru/?size="+str(size)+"&seed=2124888586&continuous=0&hub=0&random=1"
            out+="\n\n"+city.getCityDetail(size)
            markup = types.ReplyKeyboardRemove(selective=False)
            bot.send_message(chat_id, out, parse_mode="HTML", reply_markup=markup)
        else:
            step = 0
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            itembtn1 = types.KeyboardButton('Yes')
            itembtn2 = types.KeyboardButton('No')
            markup.add(itembtn1, itembtn2)
            out = "Do your city contain <b>"+MAP_STEP[step]+"</b>?"
            msg = bot.send_message(chat_id, out, parse_mode="HTML", reply_markup=markup)
            bot.register_next_step_handler(msg,process_map_consume_detail_step,size,step+1,["No"]*len(MAP_STEP))
    except Exception as e:
        printutf8(e, ofile=sys.stderr.buffer)
        bot.reply_to(message, 'You are wrong')

def isYes(decision):
    if decision == 'Yes':
        return 1
    return 0
def process_map_consume_detail_step(message,size,step,decision):
    try:
        chat_id = message.chat.id
        
        if step >= len(MAP_STEP):
            #rispondi
            out = "Hai scelto questi dettagli "+str(decision)
            out = "http://fantasycities.watabou.ru/?size="+str(size)+"&seed=2124888586&continuous=0&hub=0&random=0"
            for i in range(0,len(decision)):
                out+="&"+MAP_STEP[i].replace(' ','').lower()+"="+str(isYes(decision[i]))
            #http://fantasycities.watabou.ru/?size=17&seed=2124888586&continuous=0&hub=0&random=0&citadel=1&plaza=1&temple=1&walls=1&shantytown=0&river=0&coast=1
            out+="\n\n"+city.getCityDetail(size)
            markup = types.ReplyKeyboardRemove(selective=False)
            bot.send_message(chat_id, out, parse_mode="HTML", reply_markup=markup)
        else:
            decision[step] = message.text
            printutf8("MAP decision["+str(step)+"]: "+str(decision[step]), ofile=sys.stderr.buffer)
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            itembtn1 = types.KeyboardButton('Yes')
            itembtn2 = types.KeyboardButton('No')
            markup.add(itembtn1, itembtn2)
            out = "Do your city contain <b>"+MAP_STEP[step]+"</b>?"
            msg = bot.send_message(chat_id, out, parse_mode="HTML", reply_markup=markup)
            bot.register_next_step_handler(msg,process_map_consume_detail_step,size,step+1,decision)
    except Exception as e:
        printutf8(e, ofile=sys.stderr.buffer)
        bot.reply_to(message, 'You are wrong')

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
