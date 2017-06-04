# -*- coding: utf-8 -*-
import pyowm

def todo(City = ''):
    if City != '':
        owm = pyowm.OWM('6f6869b322d45dab227e1947d77423dd')
        observation = owm.weather_at_place(City + ',rus')
        w = (observation.get_weather()).get_temperature('celsius')
        return 'Сейчас в ' + City + ': ' + str(w['temp']) + ' градусов'
    else:
        return 'Какой город интересует?'

if __name__ == "__main__":
    print(todo('Novosibirsk'))
