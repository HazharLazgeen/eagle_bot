from binance_client import client
import pandas as pd

def time_date():
    time_stamp = client.get_server_time()
    date_time = pd.to_datetime(time_stamp["serverTime"], unit = "ms")
    _year = date_time.strftime("%y")
    _year = int(_year)
    _month = date_time.strftime("%m")
    _month = int(_month)
    _day = date_time.strftime("%d")
    _day = int(_day)


    _hour = date_time.strftime("%H")
    _hour = int(_hour)
    _minute = date_time.strftime("%M")
    _minute = int(_minute)
    _secand = date_time.strftime("%S")
    _secand = int(_secand)

    #print(time)

    #print(str(year_) +"/"+str(month_)+"/"+str(day_) +"      "+str(hour_)+":"+str(min_)+":"+str(sec_))
    return date_time, time_stamp , _year, _month, _day, _hour, _minute, _secand


def symbol() :
    nl = "%0D%0A" 
    hash = "%20%23"
    pracant = "%20%25"

    return nl, hash ,pracant

def Calc_time(time_stamp):
    date_time = pd.to_datetime(time_stamp, unit = "ms")
    _secand = date_time.strftime("%S")
    _secand = int(_secand)

    return _secand

 
"""Tb.send_msg("FIND SIGNAL🚀 "+nl+
                    "----------------------------"+nl+
                    "Ticker: "+hash+ticker+nl+
                    "Alerts 24h: "+alerts_24h+nl+
                    "Alerts 1h: "+alerts_1h+nl+
                    "Price: "+Last_price+nl+
                    "New VOL 1h: "+round(pct_New_Volume_1h,1)+"PCT"+nl)"""