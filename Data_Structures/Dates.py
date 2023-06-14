from datetime import date, datetime
import math
import pandas as pd

print("Enter a date:")
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
year = int(input("Enter the year: "))

dte = date(year, month, day)
print(dte)
dtedays = pd.Timestamp(year, month, day)

print("Enter another date:")
month2 = int(input("Enter the month: "))
day2 = int(input("Enter the day: "))
year2 = int(input("Enter the year: "))

dte2 = date(year2, month2, day2)
print(dte2)
dte2days = pd.Timestamp(year2, month2, day2)

if year > year2:
    difyear = year-year2
    if month >= month2:
        difmonth = month-month2
    if month < month2:
        difmonth = month2-month
        monthsbig = ((12*difyear)-difmonth)
        yearsdec = monthsbig/12
        difyear = math.floor(yearsdec)
        difmonth = monthsbig - (12*(math.floor(yearsdec)))
    if day >= day2:
        difday = day-day2
    if day < day2:
        difday = day2-day
        daysbig = ((difmonth*(dte2days.daysinmonth))-difday)
        monthsdec = daysbig/(dte2days.daysinmonth)
        difmonth = math.floor(monthsdec)
        difday = daysbig - ((dte2days.daysinmonth)*difmonth)

if year < year2:
    difyear = year2-year
    if month > month2:
        difmonth = month-month2
        monthsbig = ((12*difyear)-difmonth)
        yearsdec = monthsbig/12
        difyear = math.floor(yearsdec)
        difmonth = monthsbig - (12*(math.floor(yearsdec)))
    if month <= month2:
        difmonth = month2-month
    if day > day2:
        difday = day-day2
        daysbig = ((difmonth*(dtedays.daysinmonth))-difday)
        monthsdec = daysbig/(dtedays.daysinmonth)
        difmonth = math.floor(monthsdec)
        difday = daysbig - ((dtedays.daysinmonth)*difmonth)
    if day <= day2:
        difday = day2-day
if year == year2:
    if month > month2:
        difyear = year-year2
        if month >= month2:
            difmonth = month-month2
        if month < month2:
            difmonth = month2-month
            monthsbig = ((12*difyear)-difmonth)
            yearsdec = monthsbig/12
            difyear = math.floor(yearsdec)
            difmonth = monthsbig - (12*(math.floor(yearsdec)))
        if day >= day2:
            difday = day-day2
        if day < day2:
            difday = day2-day
            daysbig = ((difmonth*(dte2days.daysinmonth))-difday)
            monthsdec = daysbig/(dte2days.daysinmonth)
            difmonth = math.floor(monthsdec)
            difday = daysbig - ((dte2days.daysinmonth)*difmonth)
    if month2 > month:
        difyear = year2-year
        if month > month2:
            difmonth = month-month2
            monthsbig = ((12*difyear)-difmonth)
            yearsdec = monthsbig/12
            difyear = math.floor(yearsdec)
            difmonth = monthsbig - (12*(math.floor(yearsdec)))
        if month <= month2:
            difmonth = month2-month
        if day > day2:
            difday = day-day2
            daysbig = ((difmonth*(dtedays.daysinmonth))-difday)
            monthsdec = daysbig/(dtedays.daysinmonth)
            difmonth = math.floor(monthsdec)
            difday = daysbig - ((dtedays.daysinmonth)*difmonth)
        if day <= day2:
            difday = day2-day

print(difyear, "years,", difmonth, "months, and", difday, "days are between your two dates. This does not include the end day.")