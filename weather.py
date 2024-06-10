import json
from datetime import datetime as dt
from weather_data import data as dataStructure
data=json.loads(dataStructure)
print(f'1- {data}','\n')
country=data['sys']['country']
lat=data['coord']['lat']
lon=data['coord']['lon']
weatherM=data['weather'][0]['main']
weatherD=data['weather'][0]['description']
temperatureL=data["main"]['temp_min']
temperatureL1=temperatureL-273.15
temperatureM=data["main"]['temp_max']
temperatureM1=temperatureM-273.15
temperature=data["main"]['temp']
temperature1=temperature-273.15
wind=data['wind']['speed']
sunRise=data['sys']['sunrise']
sunSet=data['sys']['sunset']
sunSet1=dt.utcfromtimestamp(sunSet).strftime('%H:%M:%S')
sunSet=dt.utcfromtimestamp(sunSet)#.strftime('%H:%M:%S')
sunRise1=dt.utcfromtimestamp(sunRise).strftime('%H:%M:%S')
print(f'2- {sunSet}','\n')
sunRise=dt.utcfromtimestamp(sunRise)#.strftime('%H:%M:%S')
durationDay=sunSet-sunRise
durationDay=str(durationDay)
durationDay=durationDay[:-3]

print('3- ',f'Weather in ({country}): (lat_{lat}, lon_{lon}) is {weatherM} "{weatherD}", The temperature will be between {round(temperatureL1,1)}c° and {round(temperatureM1,1)}c°, and the Current Temperature is {round(temperature1,1)}c°.',f'The Wind speed will be around {wind} Km/h, and for today, The sun rise will be at {sunRise1} and the sun set will be at {sunSet1} so for today, the duration of the day will be {durationDay}!',sep='\n')

newDict={
    'Location': {'Latitude':str(lat) , 'Longitude': str(lon)} ,
    'Weather': str(weatherM) ,
    'Temperature':round(temperature1,1) ,
    'Wind': str(wind),
    'Sunrise': sunRise1,
    'Sunset': sunSet1,
    'Duration of the day':durationDay
}

print(newDict)

with open ('newFile.json','w') as newProgress:
    json.dump(newDict,newProgress,indent=4)

print(newProgress)
with open ('newFile.json', 'r') as read1:
    data3=read1.read()

with open('newFile.json','r')as read2:
    data2=json.load(read2)

print(f'4- {data2}','\n')
print(f'5- {data3}','\n')


Location=data2['Location']
Latitude=Location['Latitude']
Longitude=Location['Longitude']
Temperature=data2['Temperature']
Wind=data2['Wind']
Sunset=data2['Sunset']
Sunrise=data2['Sunrise']
Duration=data2['Duration of the day']
print('6- ')
print(f"Latitude: {Latitude}, Longitude: {Longitude}")
print(f"Temperature: {Temperature}")
print(f"Wind: {Wind}")
print(f"Sunset: {Sunset}")
print(f"Sunrise: {Sunrise}")
print(f"Duration of the day: {Duration}")
