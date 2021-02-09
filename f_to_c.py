"""

Name: Farenheit to celcius.py
Purpose: Convert farenheit to celcius 

Author: Zhang.J

Created: 08/02/2021

"""

#get the degrees in farenheit
degrees_farenheit = float(input("Enter the degrees in farenheit: "))

#convert farenheit to celcius
degrees_celcius = (degrees_farenheit-32) * (5/9)

print("")

#print final degrees in celcius
print("The degrees in celcius is "+ str(degrees_celcius))