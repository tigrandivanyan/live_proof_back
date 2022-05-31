import requests
import xml.etree.ElementTree as ET
import datetime as dt
import time

#http://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002

lastQuery = 0
xmlData = ''

def get_changerate(currency):
    global xmlData
    global lastQuery

    timedelta = time.time() - lastQuery
    if timedelta > 3600:
        lastQuery = time.time()
        response = get_datafromweb(3)
        if response != 0:
            xmlData = get_datafromweb(+3)
        
    data = xmlData.find(f'*[CharCode="{currency}"]')
    strvalue = data.find('Value').text
    value = float(strvalue.replace(',', '.'))
    return str(round(value, 1))

def get_datafromweb(time_zone):
    utc_time = dt.datetime.utcnow()
    offset = dt.timedelta(hours=time_zone)
    date = (utc_time + offset).strftime('%d/%m/%Y')

    url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}'
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Changerates refresh from {url}")
        data = ET.fromstring(response.text)
        return data
    else:
        return 0