# -*- coding: utf-8 -*-
import googlemaps

def todo(Place = '', location = '52 84'):
    if Place != '':
        gmap = googlemaps.Client(key="AIzaSyAus4Ta89otv2ABV-KUxUrJPc6QO_Pv0m0")
        [lat, lng] = location.split(' ')
        Resp = gmap.places(Place, location=(float(lat), float(lng)), radius=50, language='ru-RU')
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
