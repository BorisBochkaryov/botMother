# -*- coding: utf-8 -*-
import sys,os
from tg import *
from vk import *
from PyQt5 import QtCore, QtGui

def splitCode(keyVK,keyT,code):
    fT = open('tgBot.py','w')
    sdvigT = 0
    codeT = ''

    listModul = []

    fVK = open('vkBot.py','w')
    #codeVK = headVk(keyVK) + '\n' + writeVk()
    sdvigVK = 0
    msgVK = []
    respVK = []
    geoVK = []
    helpText = ''
    for line in code.split('\n'):
        k = str(line).rfind('?')
        cmdList = line[0:k].split(':=')
        i = str(cmdList[0]).find('(')
        j = str(cmdList[0]).find(')')
        cmd = cmdList[0][0:i]
        textCmd = cmdList[0][i+1:j]

        helpText +=  textCmd + '-' + line[k+1:-1] + '''
'''
        rezT = ''
        if cmd == 'text':
            if cmdList[1][0] != '$':
                rezT = Tg_mes_text_if([textCmd],[cmdList[1][1:-1]],sdvigT+2)
                msgVK.append(textCmd)
                respVK.append(cmdList[1][1:-1])
            else:
                i = str(cmdList[0]).find('(')
                cmdName = cmdList[1][1:i+1]
                cmdText = cmdList[1][i+2:-1]
                if cmdName == 'kurs':
                    listModul.append('kurs')
                    msgVK.append(textCmd)
                    #rezT = 'kurs:' + cmdText
                    respVK.append('kurs:' + cmdText)

        elif cmd == 'geo':
            #listModul.append('geo')
            if cmdList[1][0] == '$':
                i = str(cmdList[0]).find('(')
                cmdName = cmdList[1][1:i+1]
                cmdText = cmdList[1][i+2:-1]
                #if cmdName == 'geo':
                    #rezT = '1234\n'
        if len(rezT) > 0:
            for code_line in rezT.split('\n'):
                codeT = codeT + sdvigT*' ' + code_line + '\n'

    codeT = Tg_tok(keyT,listModul) + Tg_mes_text_header() + codeT + Tg_mes_text_if(['help'],[str(helpText)],sdvigT+2)
    codeT = codeT + Tg_main()
    fT.write(codeT)
    fT.close()
    # print(open('tgBot.py').read())
    # f.close()

    #codeVK = codeVK + '\n' + mainVk()
    msgVK.append('help')
    respVK.append(helpText)
    fVK.write(vkBot(keyVK,msgVK,respVK,listModul))
    fVK.close()

    # print(open('vkBot.py').read())

    os.system("kill -9 `ps -ax | grep vkBot.py | awk '{print $1}'`")
    os.system("kill -9 `ps -ax | grep tgBot.py | awk '{print $1}'`")
    os.system("python3 vkBot.py&")
    os.system("python3 tgBot.py&")
