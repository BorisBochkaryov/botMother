# -*- coding: utf-8 -*-
import sys
from tg import *
from vk import *
from PyQt5 import QtCore, QtGui

def splitCode(keyVK,keyT,code):
    fT = open('tgBot.py','w')
    codeT = Tg_tok(keyT) + Tg_mes_text_header()
    sdvigT = 0

    fVK = open('vkBot.py','w')
    #codeVK = headVk(keyVK) + '\n' + writeVk()
    sdvigVK = 0
    msgVK = []
    respVK = []
    helpText = ''
    for line in code.split('\n'):
        temp = line.split('?')
        cmdList = temp[0].split(':=')
        i = str(cmdList[0]).find('(')
        j = str(cmdList[0]).find(')')
        cmd = cmdList[0][0:i]
        textCmd = cmdList[0][i+1:j]

        helpText = helpText + textCmd + '-' + temp[1][1:-1] + '''
'''
        rezT = ''
        if cmd == 'text':
            if cmdList[1][0] != '{':
                rezT = Tg_mes_text_if([textCmd],[cmdList[1][1:-1]],sdvigT+2)
                #rezVK = vkBot(keyVK, )
                msgVK.append(textCmd)
                respVK.append(cmdList[1][1:-1])
            else:
                #for tmp in cmdList[1].split('\n'):
                #    listRes.append(tmp)
                rezT = Tg_mes_text_if([textCmd],[cmdList[1][1:-1]],sdvigT+2)

        for code_line in rezT.split('\n'):
            codeT = codeT + sdvigT*' ' + code_line + '\n'

    codeT = codeT + Tg_mes_text_if(['help'],[str(helpText)],sdvigT+2)
    codeT = codeT + Tg_main()
    fT.write(codeT)
    fT.close()
    # print(open('tgBot.py').read())
    # f.close()

    #codeVK = codeVK + '\n' + mainVk()
    msgVK.append('help')
    respVK.append(helpText)
    fVK.write(vkBot(keyVK,msgVK,respVK))
    fVK.close()

    # print(open('vkBot.py').read())

    os.system("kill -9 `ps -ax | grep \"thon vkBot.py\" | awk '{print $1}'`")
    os.system("kill -9 `ps -ax | grep \"thon tgBot.py\" | awk '{print $1}'`")
    os.system("python3 vkBot.py&")
    os.system("python3 tgBot.py&")
