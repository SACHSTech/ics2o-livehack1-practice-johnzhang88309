"""
--------------------------------------------------------
Name: Hours to days and hours.py
Purpose: Convert hours to days and hours

Author: Zhang.J

Created: 08/02/2021
--------------------------------------------------------
"""

#find out number of hours from the user
hours = int(input("Enter the amount of hours: "))

#convert hours to days and hours 
days = (hours//24)
remaining_hours = hours%24

print("")

#print the days and hours together 
print ("The total days and hours is " + (str(days)) + " days " + (str(remaining_hours)) + " hours")