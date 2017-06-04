# -*- coding: utf-8 -*-
import googlemaps

def todo(Place = '', lat = 54.862834, lng = 32.089386):
    if Place != '':
        gmap = googlemaps.Client(key="AIzaSyAus4Ta89otv2ABV-KUxUrJPc6QO_Pv0m0")
        Resp = gmap.places(Place, location=(lat, lng), radius=200, language='ru-RU')
        if Resp['status'] == 'OK':
            Msg = []
            for Item in Resp['results']:
                Msg.append([Item['formatted_address'], Item['geometry']['location']['lat'], Item['geometry']['location']['lng'] ])
            return Msg
        else:
            return 'Error'
    else:
        return "Что искать?"

if __name__ == '__main__':
    # bot.polling(none_stop=True)
    print(todo('Сбербанк'))
