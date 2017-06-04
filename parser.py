# -*- coding: utf-8 -*-
import sys,os
from tg import *
from vk import *
from PyQt5 import QtCore, QtGui

def splitCode(keyVK,keyT,code,fTg,fVk):
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

        helpText +=  textCmd + '-' + line[k+2:-1] + '''
'''
        rezT = ''
        #cmd([textCmd]):=cmdList[1]
        if cmd == 'text':
            if cmdList[1][0] != '$':
                listTi = []
                listCmd = []
                if textCmd.find(','):
                    for textCmdI in textCmd.split(','):
                        listTi.append(textCmdI)
                        listCmd.append(cmdList[1][1:-1])
                        msgVK.append(textCmdI)
                        respVK.append(cmdList[1][1:-1])
                    rezT = Tg_mes_text_if(listTi,respVK,sdvigT+2)
                else:
                        rezT = Tg_mes_text_if([textCmd],[cmdList[1][1:-1]],sdvigT+2)
            #cmd([textCmd]):=$cmdName(cmdText)
            else:
                i = str(cmdList[0]).find('(')
                cmdName = cmdList[1][1:i+1]
                cmdText = cmdList[1][i+2:-1]
                listTi = []
                listCmd = []
                if cmdText.find(','):
                    for textCmdI in textCmd.split(','):
                        if cmdName == 'kurs':
                            listModul.append('kurs')
                            msgVK.append(textCmdI)
                            respVK.append('kurs:' + cmdText)
                            listTi.append(textCmdI)
                            listCmd.append(cmdList[1][1:-1])
                            rezT += Tg_mes_text_if([textCmdI],['$'+cmdName + ':' + cmdText],sdvigT+2)
                else:
                    if cmdName == 'kurs':
                        listModul.append('kurs')
                        msgVK.append(textCmd)
                        rezT = Tg_mes_text_if([textCmd],['$'+cmdName + ':' + cmdText],sdvigT+2)
                        respVK.append('kurs:' + cmdText)
        #cmd([textCmd]):=$cmdName(cmdText)
        elif cmd == 'geo':
            if cmdList[1][0] == '$':
                i = str(cmdList[0]).find('(')
                cmdName = cmdList[1][1:i+1]
                cmdText = cmdList[1][i+2:-1]
                listTi = []
                listCmd = []
                if textCmd.find(','):
                    for textCmdI in textCmd.split(','):
                    #    listModul.append('geo')
                        msgVK.append(textCmdI)
                        respVK.append(cmdList[1][1:-1])
                        listTi.append(textCmdI)
                        listCmd.append(cmdList[1][1:-1])
                        rezT += Tg_mes_text_if([textCmdI],['$'+cmdName + ':' + cmdText],sdvigT+2)

                else:
                    #    listModul.append('geo')
                        msgVK.append(textCmd)
                        respVK.append('geo:' + cmdText)
                        rezT = Tg_mes_text_if([textCmd],['$'+cmdName + ':' + cmdText],sdvigT+2)
        if len(rezT) > 0:
            for code_line in rezT.split('\n'):
                codeT = codeT + sdvigT*' ' + code_line + '\n'

    listModul = list(set(listModul))

#for Telegram:
    codeT = Tg_tok(keyT,listModul) + Tg_mes_text_header() + codeT + Tg_mes_text_if(['help'],[str(helpText)],sdvigT+2)
    codeT = codeT + Tg_main()
    fT.write(codeT)
    fT.close()

#for VK:
    msgVK.append('help')
    respVK.append(helpText)
    fVK.write(vkBot(keyVK,msgVK,respVK,listModul))
    fVK.close()

#start bot
    if fVk != '0':
        os.system("kill -9 `ps -ax | grep vkBot.py | awk '{print $1}'`")
        os.system("python3 vkBot.py&")
    if fT != '0':
        os.system("kill -9 `ps -ax | grep tgBot.py | awk '{print $1}'`")
        os.system("python3 tgBot.py&")
