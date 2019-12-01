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
GND -> Pin 14 (Ground)
VCC -> Pin 16 (GPIO 23)
SIG -> Pin 18 (GPIO 24)

'''

# Imports
import time
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

# DarkSkies API Setup
location = ("51.476440", "-0.198166")
secret = "43f8f3120c5aace69ec2a58b73313b38"

# Test Readings
def logdata():
  now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
  sensor.get_sensor_data()
  temp = "{0:.1f} C".format(sensor.data.temperature)
  press = "{0:.1f} hPa".format(sensor.data.pressure)
  hum = "{0:.1f} %RH".format(sensor.data.humidity)
  with open('data/sensordata.csv', 'a', ) as file:
    writer = csv.writer(file)
    writer.writerow([now, temp, press, hum])
  print('New data logged')
  pushdata()


# GitHub push function from stackoverflow.com/questions/38594717
def pushdata(token='e33eeb41a8a264e5c2e737db2383a37b494a32af'):

  g = Github(token)
  repo = g.get_user().get_repo('soilsensor')

  file_list = [
    'data/sensordata.csv',
    'data/notes.txt'
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
  print('Updated data pushed to GitHub')

  
print('Running test script, use CTRL+C to cancel')
while True:
  logdata()
  time.sleep(10)
