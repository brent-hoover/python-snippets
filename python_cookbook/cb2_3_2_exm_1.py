import datetime, calendar
lastFriday = datetime.date.today()
while lastFriday.weekday() != calendar.FRIDAY:
    lastFriday -= datetime.date.resolution
print lastFriday.strftime('%d-%b-%Y')
