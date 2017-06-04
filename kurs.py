# -*- coding: utf-8 -*-
import os, sys
from pycbrf.toolbox import ExchangeRates
from datetime import *

def todo(Arg = ''):
    if Arg != '':
        dataQuery = datetime.now().strftime("%Y-%m-%d")
        rates = ExchangeRates(dataQuery)
        response = 'Курс ' + Arg + ' на ' + datetime.now().strftime("%d-%m-%Y") + ': '
        response += str(float(rates[Arg].rate)) + ' руб'
        return response
    else:
        return "Какая валюта интересует?"

if __name__ == "__main__":
    print(todo())
