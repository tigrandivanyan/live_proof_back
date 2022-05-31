import requests
import datetime as dt

def get_time(time_zone):
    utc_time = dt.datetime.utcnow()
    offset = dt.timedelta(hours=time_zone)
    return (utc_time + offset).strftime('%H:%M')

def get_date(time_zone):
    utc_time = dt.datetime.utcnow()
    offset = dt.timedelta(hours=time_zone)
    return (utc_time + offset).strftime('%d.%m.%y')
