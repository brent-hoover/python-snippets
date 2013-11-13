import datetime, calendar
today = datetime.date.today()
targetDay = calendar.FRIDAY
thisDay = today.weekday()
deltaToTarget = (thisDay - targetDay) % 7
lastFriday = today - datetime.timedelta(days=deltaToTarget)
print lastFriday.strftime('%d-%b-%Y')
