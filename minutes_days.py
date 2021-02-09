"""
--------------------------------------------------------
Name: Minutes to days, hours and minutes calculator.py
Purpose: Coverting mnutes to days, hours and minutes

Author: Zhang.J

Created: 08/02/2021
--------------------------------------------------------
"""

#Find out the amount of minutes
minutes=int(input("Enter the amount of minutes: "))

#Calculating days, hours and minutes 
days = (minutes//1440)
hours = (minutes//60 - days * 24)
remaining_minutes = minutes - (days * 1440) - (hours*60)

#Final print statement
print("Days:",days,"Hours:",hours,"Minutes:",remaining_minutes)

