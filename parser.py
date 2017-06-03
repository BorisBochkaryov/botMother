# -*- coding: utf-8 -*-
import sys
from tg import *
from vk import *

def splitCode(keyVK,keyT,code):
    fT = open('tgBot.py','w')
    codeT = Tg_tok(keyT) + Tg_mes_text_header()
    sdvigT = 0

    fVK = open('vkBot.py','w')
    #codeVK = headVk(keyVK) + '\n' + writeVk()
    sdvigVK = 0
    msgVK = []
    respVK = []
    for line in code.split('\n'):
        cmdList = line.split(':=')
        i = str(cmdList[0]).find('(')
        j = str(cmdList[0]).find(')')
        cmd = cmdList[0][0:i]
        textCmd = cmdList[0][i+1:j]
        listRes = []
        if cmd == 'text':
            if cmdList[1][0] != '{':
                rezT = Tg_mes_text_if([textCmd],[cmdList[1][1:-1]],sdvigT+2)
                #rezVK = vkBot(keyVK, )
                msgVK.append(textCmd)
                respVK.append(cmdList[1][1:-1])
            else:
                #for tmp in cmdList[1].split('\n'):
                #    listRes.append(tmp)
                rezT = Tg_mes_text_if([textCmd],cmdList[1][1:-1],sdvigT+2)

        for code_line in rezT.split('\n'):
            codeT = codeT + sdvigT*' ' + code_line + '\n'

    codeT = codeT + Tg_main()
    fT.write(codeT)
    fT.close()
    #print(open('tgBot.py').read())
    #f.close()

    #codeVK = codeVK + '\n' + mainVk()

    fVK.write(vkBot(keyVK,msgVK,respVK))
    fVK.close()

    print(open('vkBot.py').read())
