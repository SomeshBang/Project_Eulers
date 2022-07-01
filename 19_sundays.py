# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# import datetime

leap = 1
count = 0
for year in range(1901,2001):
    if year % 4 == 0:
        leap = 0
    else:
        leap = 1
    for month in range(1,13):
        if leap == 0 and month == 2:
            for date in range(1,30):  # i.e 29 leap year 
                findDay = datetime.date(year,month,date)
                day = findDay.weekday()
                if date == 1 and day == 6:
                    count +=1

        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            for date in range(1,32): #i.e 31 days
                findDay = datetime.date(year,month,date)
                day = findDay.weekday()
                if date == 1 and day == 6:
                    count+=1

        elif month == 4 or month == 6 or month == 9 or month == 11:
            for date in range(1,31):
                findDay = datetime.date(year,month,date)
                day = findDay.weekday()
                if date == 1 and day == 6:
                    count+=1

        else:
            for date in range(1,29):  #i.e 28 days of feb not a leap year
                findDay = datetime.date(year,month,date)
                day = findDay.weekday()
                if date == 1 and day == 6:
                    count+=1

print(count)