# -*- coding: utf-8 -*-
import sys,os
from tg import *
from vk import *
from PyQt5 import QtCore, QtGui

def splitCode(keyVK,keyT,code,fTg,fVk):
    flagCode = 0
    flagTGBot = 0
    flagVKBot = 0
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
    for line in code.lower().split('\n'):
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
                q = str(cmdList[1]).find('(')
                cmdName = cmdList[1][1:q]
                cmdText = cmdList[1][q+1:-1]
                listTi = []
                listCmd = []
                if cmdText.find(','):
                    for textCmdI in textCmd.split(','):
                        # print(cmdName)
                        if cmdName == 'kurs' or cmdName == 'weather' or cmdName == 'geo':
                            listModul.append(cmdName)
                            msgVK.append(textCmdI)
                            respVK.append(cmdName + ':' + cmdText)
                            listTi.append(textCmdI)
                            listCmd.append('$'+cmdName + ':' + cmdText)
                        rezT = Tg_mes_text_if(listTi,listCmd,sdvigT+2)
                else:
                    if cmdName == 'kurs' or cmdName == 'weather' or cmdName == 'geo':
                        listModul.append(cmdName)
                        msgVK.append(textCmd)
                        respVK.append(cmdName + ':' + cmdText)
                        rezT = Tg_mes_text_if([textCmd],['$'+cmdName + ':' + cmdText],sdvigT+2)

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
                        listModul.append(cmdName)
                        msgVK.append(textCmdI)
                        respVK.append(cmdList[1][1:-1])
                        listTi.append(textCmdI)
                        listCmd.append('$'+cmdName + ':' + cmdText)
                    rezT = Tg_mes_text_if(listTi,listCmd,sdvigT+2)
                else:
                        listModul.append(cmdName)
                        msgVK.append(textCmd)
                        respVK.append(cmdName + ':' + cmdText)
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
    flagCode = 1
#start bot
    if fVk != '0':
        os.system("kill -9 `ps -ax | grep vkBot.py | awk '{print $1}'`")
        os.system("python3 vkBot.py&")
        flagVKBot = 1
    if fTg != '0':
        os.system("kill -9 `ps -ax | grep tgBot.py | awk '{print $1}'`")
        os.system("python3 tgBot.py&")
        flagTGBot = 1
    return [flagCode,flagVKBot,flagTGBot]
