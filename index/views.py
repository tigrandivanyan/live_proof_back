from django.shortcuts import render, HttpResponse
from weather.service import get_weather
from gtime.service import get_time, get_date
from currency.service import get_changerate, get_changerateKZ
import json
#msk-524901
#london-2643743
#NY-5128581

def index(request):
    #weather = get_weather('524901')
    #date = get_date(+3)
    #time = get_time(+3)
    #changerate = get_changerate('EUR')
    #context = {
    #            'weather': weather,
    #            'date': date,
    #            'time': time,
    #            'changerate': changerate,                            
    #            }
    jsonFront = {
                    "cities":[
                        {
                            "name":"Москва",
                            "weather":get_weather('524901'),
                            "time":get_time(+3),
                            "additional":"data streamed from openweathermap.org",
                            "backgroundImageName":"moscow.jpg"
                        },
                        {
                            "name":"Нью-Йорк",
                            "weather":get_weather('5128581'),
                            "time":get_time(-5),
                            "additional":"data streamed from openweathermap.org",
                            "backgroundImageName":"newYork.jpg"
                        },
                        {
                            "name":"Лондон",
                            "weather":get_weather('2643743'),
                            "time":get_time(0),
                            "additional":"data streamed from openweathermap.org",
                            "backgroundImageName":"london.jpg"
                        },
                    ],
                    "currencies":{
                        "date":get_date(+3),
                        "backgroundImageName":"currency.jpg",
                        "currency1":{
                            "name":"USD",
                            "value":get_changerate('USD')
                        },
                        "currency2":{
                            "name":"EUR",
                            "value":get_changerate('EUR')
                        },
                        "additional":"data streamed from www.cbr.ru"
                    }
            
                }


    #return render(request, 'index.html', context)
    return HttpResponse(json.dumps(jsonFront))
