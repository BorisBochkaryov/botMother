# -*- coding: utf-8 -*-
#from configs import *
from telebot import *

# bot = TeleBot(token)

# @bot.message_handler(content_types=['text'])
# def comands(message):
#     bot.send_message(message.chat.id, message.text + ", ты пидор")

def Tg_tok(token):
    return '''from telebot import *
bot = TeleBot(\'''' + str(token) + '''\')\n
'''
def Tg_main():
    return '''if __name__ == '__main__':
    bot.polling(none_stop=True)
'''
def Tg_mes_text_header():
    return '''@bot.message_handler(content_types  = ['text'])
def comands(message):
'''
def Tg_mes_text_send(mes,sdvig):
    return  sdvig*' '+'''bot.send_message(message.chat.id, \'\'\'''' + str(mes)+ '''\'\'\')
'''
def Tg_mes_text_if(mas,otv,sdvig):
    log = ''
    for item,item2 in zip(mas,otv):
        log += sdvig*' '+'''if message.text == ''' + '''\''''+ item + '''\'''' + ''':
''' +Tg_mes_text_send(item2,sdvig+2) +'\n'
    return log


# if __name__ == '__main__':
#     bot.polling(none_stop=True)
