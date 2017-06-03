# -*- coding: utf-8 -*-
# 'body' - текст сообщения
# 'id' - id сообщения
# 'user_id' - id пользователя
# 'date' - дата сообщения

# формирование заголовка бота
def headVk(Token):
    return '''import time, vk_api
vk = vk_api.VkApi(token = \'''' + Token + '''\')
values = {'out': 0, 'count': 100, 'time_offset': 60}'''

# формирование функции отправки сообщения
def writeVk():
    return '''def writeMsg(user_id, msg):
    vk.method('messages.send', {'user_id':user_id, 'message':msg})'''

# формирование условий
def ifVk(Msg, Response, Item):
    if Item >= len(Msg):
        return ''
    else:
        Resp = Response[Item]
        return '''        if item['body'] == "''' + Msg[Item] + '''":
                print(item['body'], ' >>from<< ', item['user_id'])
                writeMsg(item['user_id'],\"''' + Resp + '''\")
    ''' + ifVk(Msg, Response, Item + 1)

# формирование приема сообщений
def readVk(Msg, Response):
    readMsg = '''def readMsg():
    while True:
        response = vk.method('messages.get', values)
        if response['items']:
            values['last_message_id'] = response['items'][0]['id']
        for item in response['items']:
    '''

    ifVkStr = ifVk(Msg, Response, 0)

    readMsg += ifVkStr + '''    time.sleep(1)'''
    return readMsg

def mainVk():
    return '''if __name__ == \"__main__\":
    readMsg()'''

def vkBot(Token, Msg, Resp):
    Bot = headVk(Token) + "\n"
    Bot += writeVk() + "\n"
    Bot += readVk(Msg,Resp) + "\n"
    Bot += mainVk() + "\n"
    return Bot

if __name__ == "__main__":
    # readMsg()
    print(vkBot("198ea0ffd479982bf90ff58d16f0d12d08fa470b1835310fe14e035a23bb3d000aed0caa6761006fdd67c", ["Hello", "Bye"], ["Bye", "Ok"]))
