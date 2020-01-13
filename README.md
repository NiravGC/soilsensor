# Soil Sensor Coursework
This project uses a Raspberry Pi Zero W to collect three sets of data.

> * **Soil Moisture**    Taken using a SparkFun soil moisture probe   
> * **Room Conditions**  Sampled using a BME680 temperature, pressure, and humidity sensor   
> * **Local Weather**    Pulled from the DarkSkies API  

### Dependencies
In order to run the data collection script `sensing.py` the following libraries must be installed.
> * RPi.GPIO  
> * bme680  
> * adafruit-ads1x15  
> * PyGithub  

> **Note:** the `sensing.py` script must be run in **Python 3** to function properly.

For data collection, only `sensing.py` need to be run - `historic.py` can be used to view historic DarkSkies weather data in the case that the CSV has failed to populate certain weather cells (occurs in cases where there is a connection issue during sampling).

### Data Files
The file `allData.csv` contains all data that has been pushed by the `sensing.py` script. This includes some erroneous values that were added during setup and is included in the repository for completeness. The file `rawData.csv` is the rawData across the intended sample period and is the file used in data analysis and visualisation.

### Data Analysis
All data analysis has been conducted within the `Data Analysis.ipynb` Jupyter Notebook file and can be downloaded or viewed directly within Github.

### Interface
A sample interface for viewing up-to-date sample data is available at https://niravgc.github.io/soilsensor/. Files used to display this interface are contained within the `/docs` folder. 
