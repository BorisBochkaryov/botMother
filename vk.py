# -*- coding: utf-8 -*-
# 'body' - текст сообщения
# 'id' - id сообщения
# 'user_id' - id пользователя
# 'date' - дата сообщения

# формирование заголовка бота
def headVk(Token, Modules):
    Import = ''
    for X in Modules:
        M = (X.split(':'))[0]
        Import += 'import ' + M + '\n'
    return Import + '''
import time, vk_api, sys
vk = vk_api.VkApi(token = \'''' + Token + '''\')
values = {'out': 0, 'count': 100, 'time_offset': 60}'''

# формирование функции отправки сообщения
def writeVk():
    return '''def writeMsg(user_id, msg):
    if type(msg) == list:
        for X in msg:
            vk.method('messages.send', {'user_id':user_id, 'message': X[0], 'lat': X[1], 'long': X[2]})
    else:
        vk.method('messages.send', {'user_id':user_id, 'message':msg})'''

# формирование условий
def ifVk(Msg, Response, Item, Modules):
    if Item >= len(Msg):
        return ''
    else:
        Resp = Response[Item]
        if ':' in Resp:
            M = (Resp.split(':'))[0]
            A = (Resp.split(':'))[1]
            if M in Modules:
                return '''        if item['body'] == "''' + Msg[Item] + '''":
                writeMsg(item['user_id'], getattr(sys.modules["''' + M + '''"], "todo")("''' + A + '''"))
    ''' + str(ifVk(Msg, Response, Item + 1, Modules))
            else:
                return '' + str(ifVk(Msg, Response, Item + 1, Modules))
        else:
            return '''        if item['body'].lower() == "''' + Msg[Item].lower() + '''":
                writeMsg(item['user_id'],\'\'\'''' + Resp + '''\'\'\')
    ''' + str(ifVk(Msg, Response, Item + 1, Modules))

# формирование приема сообщений
def readVk(Msg, Response, Modules):
    readMsg = '''def readMsg():
    while True:
        response = vk.method('messages.get', values)
        if response['items']:
            values['last_message_id'] = response['items'][0]['id']
        for item in response['items']:
            print(item)
            if 'geo' in item:
                writeMsg(item['user_id'], getattr(sys.modules["geo"], "todo")("''' + "Сбербанк" + '''", item['geo']['coordinates']))
    '''

    ifVkStr = ifVk(Msg, Response, 0, Modules)

    readMsg += ifVkStr + '''    time.sleep(1)'''
    return readMsg

# формирование main для бота
def mainVk():
    return '''if __name__ == \"__main__\":
    readMsg()'''

def vkBot(Token, Msg, Resp, Modules):
    Bot = headVk(Token, Modules) + "\n"
    Bot += writeVk() + "\n"
    Bot += readVk(Msg,Resp,Modules) + "\n"
    Bot += mainVk() + "\n"
    return Bot

if __name__ == "__main__":
    print(vkBot("198ea0ffd479982bf90ff58d16f0d12d08fa470b1835310fe14e035a23bb3d000aed0caa6761006fdd67c",
        ["Hello", "Bye", "курс мне", "что с Европой", "погода", "банкомат"],
        ["Bye1", "Ok", "kurs:USD", "kurs:EUR", "weather:Novosibirsk","geo:Сбербанк"],
        ["kurs", "weather","geo"]))
