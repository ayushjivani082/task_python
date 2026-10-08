# Leap Year Finder

import calendar

year = int(input("Enter year: "))

if calendar.isleap(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


# Appointment System and Study Reminder


import calendar

day = input("Enter day of the week: ").lower()

if day == "monday":
    print("Appointment: 10:00 AM")
    print("Study Reminder: Python Practice")

elif day == "tuesday":
    print("Appointment: 11:00 AM")
    print("Study Reminder: SQL Practice")

elif day == "wednesday":
    print("Appointment: 2:00 PM")
    print("Study Reminder: Data Science")

elif day == "thursday":
    print("Appointment: 10:30 AM")
    print("Study Reminder: Python Project")

elif day == "friday":
    print("Appointment: 12:00 PM")
    print("Study Reminder: GitHub Practice")

elif day == "saturday":
    print("Appointment: 11:00 AM")
    print("Study Reminder: Revision")

elif day == "sunday":
    print("No Appointment")
    print("Study Reminder: Revise Weekly Topics")

else:
    print("Please enter a valid day")

