# Soil Sensor Coursework
This project uses a Raspberry Pi Zero W to collect three sets of data.

> * **Soil Moisture**    Taken using a SparkFun soil moisture probe   
> * **Room Conditions**  Sampled using a BME680 temperature, pressure, and humidity sensor   
> * **Local Weather**    Pulled from the DarkSkies API  

### Dependencies
In order to run the data collection script `sensing.py` the following libraries must be installed.
> RPi.GPIO  
> bme680  
> adafruit-ads1x15  
> PyGithub  

> **Note:** the `sensing.py` script must be run in **Python 3** to function properly.
