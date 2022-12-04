import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Zadania Python

temperatureWarsawDataFrame = pd.DataFrame(
    {'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
               'November', 'December'],
     'WarsawTemperature': [-2, -1, 3, 9, 14, 18, 19, 18, 14, 9, 3, 0]})
temperatureMiamiDataFrame = pd.DataFrame(
    {'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
               'November', 'December'],
     'MiamiTemperature': [7, 9, 12, 16, 22, 27, 28, 27, 25, 18, 12, 7]})

plt.plot(temperatureWarsawDataFrame['Month'], temperatureWarsawDataFrame['WarsawTemperature'], color='red')
plt.plot(temperatureMiamiDataFrame['Month'], temperatureMiamiDataFrame['MiamiTemperature'], 'o-g')
plt.xlabel("Months")
plt.ylim(-5, 30)
plt.tick_params(axis='x', labelsize=5)
plt.ylabel("Temperature in celcius")
plt.title("Average temperature in every month")
plt.legend(['Temperature in Warsaw', 'Temperature in Miami'], loc='upper left')
plt.savefig("AverageTemperature.png", dpi=600)