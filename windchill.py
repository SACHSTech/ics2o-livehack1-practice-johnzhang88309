"""
--------------------------------------------------------
Name: Windchill calculator.py
Purpose: Calculating windchill

Author: Zhang.J

Created: 08/02/2021
--------------------------------------------------------
"""

#find out the temperature(celcius)and the wind speed in km/h
celcius = float(input("Temperature in celcius: "))
wind = float(input("Wind speed in km/h: "))

print("")

#calculate windchill
windchill = (13.12 + (0.6215 * celcius) - (11.37 * wind ** 0.16) + (0.3965 * celcius * wind ** 0.16))
print("The windchill factor is " + str(windchill))