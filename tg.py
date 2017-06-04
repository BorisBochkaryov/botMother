# -*- coding: utf-8 -*-
#from configs import *
from telebot import *

# bot = TeleBot(token)

# @bot.message_handler(content_types=['text'])
# def comands(message):
#     bot.send_message(message.chat.id, message.text + ", ты пидор")

def Tg_tok(token,listModul):
    tmp = ''
    for i in listModul:
        tmp += 'import '+ i + '\n'
    return tmp + '''\nfrom telebot import *
bot = TeleBot(\'''' + str(token) + '''\')\n
'''
def Tg_main():
    return '''if __name__ == '__main__':
    bot.polling(none_stop=True)
'''

def Tg_mes_location_header():
    return '''@bot.message_handler(content_types  = ['location'])
def geocomands(message):
    location = str(message.location.latitude) + ' ' + str(message.location.longitude)
    listBank = getattr(sys.modules["geo"], "todo")("''' + "Сбербанк" + '''", location)
    for X in list(reversed(listBank)):
        bot.send_location(message.chat.id, latitude=X[1], longitude=X[2])
'''

def Tg_mes_text_header():
    return '''@bot.message_handler(content_types  = ['text'])
def comands(message):
'''
def Tg_mes_text_send(mes,sdvig):
    return  sdvig*' '+'''bot.send_message(message.chat.id, ''' + str(mes)+ ''')
'''

def Tg_mes_text_if(mas,otv,sdvig):
    log = ''
    for item,item2 in zip(mas,otv):
        if item2[0] == '$':
            item2 = item2[1:]
            if ':' in item2:
                M = (item2.split(':'))[0]
                A = (item2.split(':'))[1]
                log += sdvig*' '+'''if message.text.lower() == "''' + item + '''":\n'''+ Tg_mes_text_send('''getattr(sys.modules["''' + M + '''"], "todo")("''' + A + '''")''',sdvig+2)
        else:
            log += sdvig*' '+'''if message.text.lower() == ''' + '''\''''+ item + '''\'''' + ''':
''' +Tg_mes_text_send("\'\'\'" + str(item2) + "\'\'\'",sdvig+2) +'\n'
    return log

if __name__ == '__main__':
#     bot.polling(none_stop=True)
    print(Tg_tok("398702729:AAGEbX17tBg8KBRbykgoeYbbOIX2bYWXMTc",["geo","kurs"]))
    print(Tg_mes_location_header())
    print(Tg_mes_text_header())
    print(Tg_mes_text_if(["txt1","txt2"], ["t1","t2"], 1))
    print(Tg_main())
