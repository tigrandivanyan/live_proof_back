import requests
import json
import time

#Версия от 1.06.22.  
#Теперь погода запрашивается для любых городов по ID c openweathermap.org
#Температура теперь округляется правильно и должна совпадать с указанной на сайте. Раньше все, что после запятой просто отбрасывалось.

lastQuery = 0
cityWeather = {}


def get_weather(id):
    global lastQuery
    global cityWeather

    newCity = False

    if cityWeather.get(id, 999) == 999:
        newCity = True
        print(f'Added city with ID - {id}')

    timeDelta = time.time() - lastQuery

    if timeDelta > 600:
        lastQuery = time.time()
        for w in cityWeather.keys():
            cityWeather[w] = get_weatherFromWeb(w)

    if newCity == True:
        cityWeather[id] = get_weatherFromWeb(id)
        lastQuery = time.time()

    return cityWeather[id]



def get_weatherFromWeb(id, api_key='a1612928218374494f0be6aa88b2c9db'):
    url = f'http://api.openweathermap.org/data/2.5/weather?id={id}&units=metric&lang=ru&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Weather refresh for ID {id} from {url}')
        r_json= json.loads(response.text)
        temperature = round(r_json['main']['temp'])
        if temperature > 0:
            return f'+{temperature}'
        else:
            return str(temperature) 