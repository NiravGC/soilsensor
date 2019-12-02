'''
The following program is used to assess a number of variables at regular four hour intervals.
Ambient data is collecteed using a BME680 temperature, pressure, and humidity sensor.
Soil moisture data is collected using a Sparkfun Soil Moisture Sensor

This data will be combined with location-specific weather data to how the water consumption
of a potted plan varies with conditions.

* Pin Reference *
BME680 Breakout - 
PWR -> Pin 1 (3.3V)
SDA -> Pin 3 (GPIO 2)
SCL -> Pin 5 (GPIO 3)
GND -> Pin 9 (Ground)

Soil Moisture Sensor -
'''

# Imports
import time
import requests
import csv
import bme680
import RPi.GPIO as GPIO
from github import Github, InputGitTreeElement
from datetime import datetime

# Temperature, Humidity, Pressure Sensor Setup
sensor = bme680.BME680()
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

# Moisture Sensor Setup
''' tbc '''
def logMoisture():
  return()
  # tbc

# Sensor Readings
def logSensor():
  sensor.get_sensor_data()
  temp = "{:.1f}".format(sensor.data.temperature)
  press = "{:.2f}".format(sensor.data.pressure)
  hum = "{:.0f}".format(sensor.data.humidity)
  print('Sensor data logged')
  return([temp, press, hum])
 
# DarkSkies API Readings
def logWeather(secret = "43f8f3120c5aace69ec2a58b73313b38", location = (["51.476440", "-0.198166"]):
  apikey = "https://api.darksky.net/forecast/{0}/{1},{2}?exclude=minutely,hourly,daily,alerts,flags&units=si".format(
    secret, location[0], location[1])
  weather = requests.get(apikey)
  localTemp = weather['currently']['temperature']               # local temperature
  localPress = weather['currently']['pressure']                 # local pressure
  localHum = weather['currently']['humidity'] * 100             # local humidity
  precipProb = weather['currently']['precipProbability'] * 100  # precipitation probability
  precipInt = weather['currently']['precipIntensity']           # precipitation intensity
  cloud = weather['currently']['cloudCover']                    # cloud cover
  print('Weather data logged')
  return([localTemp, localPress, localHum, precipProb, precipInt, cloud])

def writeData():
  now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
  sensorData = logSensor()
  weatherData = logWeather()
  allData = [now] + sensorData + weatherData
  with open('data/allData.csv', 'a', ) as file:
    writer = csv.writer(file)
    writer.writerow(allData)
  print('Data written to CSV file')
  
# GitHub push function from stackoverflow.com/questions/38594717
def pushData(token='e33eeb41a8a264e5c2e737db2383a37b494a32af'):
  g = Github(token)
  repo = g.get_user().get_repo('soilsensor')
  file_list = [
    'data/sensordata.csv'#,
    #'data/notes.txt' hack file as code is designed to work with 2+ changes (test with this removed?)
  ]       
  commit_message = 'AUTO: New data logged'
  master_ref = repo.get_git_ref('heads/master')
  master_sha = master_ref.object.sha
  base_tree = repo.get_git_tree(master_sha)
  element_list = list()
  for entry in file_list:
      with open(entry, 'rb') as input_file:
          data = input_file.read()
      element = InputGitTreeElement(entry, '100644', 'blob', data)
      element_list.append(element)
  tree = repo.create_git_tree(element_list, base_tree)
  parent = repo.get_git_commit(master_sha)
  commit = repo.create_git_commit(commit_message, tree, [parent])
  master_ref.edit(commit.sha)
  print('Data pushed to GitHub')
  
print('Running test script, use CTRL+C to cancel')
while True:
  writeData()
  sleep(30)
