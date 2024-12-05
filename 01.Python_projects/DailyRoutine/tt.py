def peaceful_time(ts,tr):
    import math
    b,a = math.modf(ts)
    d,c = math.modf(tr)
    ts = (a*60) + (b*100)
    tr = (c*60) + (d*100)
    x = 1440 - ts
    Tt = (((2/3)*(1440-ts+tr)-x))
    TT = int(Tt)
   # Divide the minutes by 60 to get the hour part
    hour = TT // 60
    # Use the modulo operator to get the remaining minutes
    minutes = TT % 60
    if minutes < 10 :
        print(f"Peaceful time starts at {hour}:0{minutes}")
    else:
        print(f"Peaceful time starts at {hour}:{minutes}")
        print("Peaceful time starts after",Tt,"minutes or",TT,"minutes or",hour,"hour",minutes,"minutes from 0:00")


# 1. Get the current location
import datetime
from suntime import Sun, SunTimeException
import requests
response = requests.get("https://ipinfo.io")
data = response.json()
print(f'Your IP address is {data["ip"]}')
print(f'Your city is {data["city"]}')
print(f'Your region is {data["region"]}')
print(f'Your country is {data["country"]}')
print(f'Your coordinates are {data["loc"]}')

location = data["loc"]
lat,long = location.split(",")
latitude = float(lat)
longitude = float(long)
print(latitude,longitude)


sun = Sun(latitude, longitude)



 # 2. Get the date of today
today = datetime.date.today()

 # 3. Get the time of sunrise and sunset today
today_sr = sun.get_local_sunrise_time(today)
today_ss = sun.get_local_sunset_time(today)
print('On {} the sun at your current location raised at {} and get down at {}.'.format(today, today_sr.strftime('%H:%M'), today_ss.strftime('%H:%M')))

# 4. Get the date of tomorrow
from datetime import date, timedelta
today = date.today() 
tomorrow = today + timedelta(days=1)

# 5. Get the time of sunrise and sunset of tomorrow
tomorrow = tomorrow# The date you want
tomorrow_sr = sun.get_local_sunrise_time(tomorrow)
tomorrow_ss = sun.get_local_sunset_time(tomorrow)
print('On {} the sun at your current location raised at {} and get down at {}.'.format(tomorrow, tomorrow_sr.strftime('%H:%M'),
tomorrow_ss.strftime('%H:%M')))

# 6. Converting the datetime.datetime object to float
sunset_of_today = today_ss.strftime('%H:%M')
sunset_of_today = sunset_of_today.replace(":",".")
sunset_of_today = float(sunset_of_today)
sunrise_of_tomorrow = tomorrow_sr.strftime('%H:%M')
sunrise_of_tomorrow = sunrise_of_tomorrow.replace(":",".")
sunrise_of_tomorrow = float(sunrise_of_tomorrow)

# 7. Calling the main function
peaceful_time(sunset_of_today,sunrise_of_tomorrow)

