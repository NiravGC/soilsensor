# Collect historic weather data for failed DarkSkies data points
# Used to fill missing weather data where applicable

# Imports
import time
import requests
import csv
import json
from datetime import datetime
 
# DarkSkies API Readings
def logWeather(time, secret = "[REMOVED]", location = ["51.476440", "-0.198166"]):
  apikey = "https://api.darksky.net/forecast/{0}/{1},{2},{3}?exclude=minutely,hourly,daily,alerts,flags&units=si".format(
    secret, location[0], location[1], time)
  try:
    weather = requests.get(apikey).json()
    localTemp = weather['currently']['temperature']               # local temperature
    localPress = weather['currently']['pressure']                 # local pressure
    localHum = weather['currently']['humidity'] * 100             # local humidity
    precipProb = weather['currently']['precipProbability'] * 100  # precipitation probability
    precipInt = weather['currently']['precipIntensity']           # precipitation intensity
    cloud = weather['currently']['cloudCover']                    # cloud cover
    # print('Weather data logged')
    return([localTemp, localPress, localHum, precipProb, precipInt, cloud])
  except requests.exceptions.ConnectionError:
    print('WARNING: Connection error - could not pull weather data')
    return(['null', 'null', 'null', 'null', 'null', 'null'])
  except:
    print('WARNING: Unknown error')
    return(['null', 'null', 'null', 'null', 'null', 'null'])

  


# Begin main function
print('Data recovery')

while True:
  inputTime = str(input("Enter desired time in UNIX timestamp: "))
  reading = logWeather(inputTime)
  print("Temperature: {}".format(reading[0]))
  print("Pressure: {}".format(reading[1]))
  print("Humidity: {}".format(reading[2]))
  print("Precipitation Probability: {}".format(reading[3]))
  print("Precipitation Intensity: {}".format(reading[4]))
  print("Cloud Cover: {}".format(reading[5]))
