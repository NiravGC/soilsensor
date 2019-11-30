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

import time
import bme680

sensor = bme680.BME680()
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
