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
                            "name":"Нур-Султан",
                            "weather":get_weather('1526273'),
                            "time":get_time(+6),
                            "additional":"data streamed from openweathermap.org",
                            "backgroundImageName":"nursultan.jpg"
                        },
                        {
                            "name":"Уральск",
                            "weather":get_weather('608668'),
                            "time":get_time(+5),
                            "additional":"data streamed from openweathermap.org",
                            "backgroundImageName":"uralsk.jpg"
                        },
                        {
                            "name":"Москва",
                            "weather":get_weather('524901'),
                            "time":get_time(+3),
                            "additional":"data streamed from openweathermap.org",
                            "backgroundImageName":"moscow.jpg"
                        },
                    ],
                    "currencies":{
                        "date":get_date(+3),
                        "backgroundImageName":"currency.jpg",
                        "currency1":{
                            "name":"USD",
                            "value":get_changerateKZ('USD')
                        },
                        "currency2":{
                            "name":"RUB",
                            "value":get_changerateKZ('RUB')
                        },
                        "additional":"data streamed from www.nationalbank.kz"
                    }
            
                }


    #return render(request, 'index.html', context)
    return HttpResponse(json.dumps(jsonFront))
