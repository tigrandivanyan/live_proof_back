import requests
import json
import time

#msk-524901
#london-2643743
#NY-5128581

lastQuery = 0
cityWeather = {'524901': 0, '2643743': 0, '5128581': 0}


def get_weather(id):
    global lastQuery
    global cityWeather

    timeDelta = time.time() - lastQuery
    if timeDelta > 600:
        print('Weather refresh')
        lastQuery = time.time()
        for w in cityWeather.keys():
            cityWeather[w] = get_weatherFromWeb(w)

    return cityWeather[id]



def get_weatherFromWeb(id, api_key='a1612928218374494f0be6aa88b2c9db'):
    url = f'http://api.openweathermap.org/data/2.5/weather?id={id}&units=metric&lang=ru&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        r_json= json.loads(response.text)
        temperature = int(r_json['main']['temp'])
        if temperature > 0:
            return f'+{temperature}'
        else:
            return str(temperature) 