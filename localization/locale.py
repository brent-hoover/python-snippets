import datetime

# ex: 09-06-12-10-01
print datetime.datetime.now().strftime("%y-%m-%d-%H-%M")

#Directive	Meaning	Notes
#%a	Locale’s abbreviated weekday name.	 
#%A	Locale’s full weekday name.	 
#%b	Locale’s abbreviated month name.	 
#%B	Locale’s full month name.	 
#%c	Locale’s appropriate date and time representation.	 
#%d	Day of the month as a decimal number [01,31].	 
#%f	Microsecond as a decimal number [0,999999], zero-padded on the left	(1)
#%H	Hour (24-hour clock) as a decimal number [00,23].	 
#%I	Hour (12-hour clock) as a decimal number [01,12].	 
#%j	Day of the year as a decimal number [001,366].	 
#%m	Month as a decimal number [01,12].	 
#%M	Minute as a decimal number [00,59].	 
#%p	Locale’s equivalent of either AM or PM.	(2)
#%S	Second as a decimal number [00,61].	(3)
#%U	Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.	(4)
#%w	Weekday as a decimal number [0(Sunday),6].	 
#%W	Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.	(4)
#%x	Locale’s appropriate date representation.	 
#%X	Locale’s appropriate time representation.	 
#%y	Year without century as a decimal number [00,99].	 
#%Y	Year with century as a decimal number.	 
#%z	UTC offset in the form +HHMM or -HHMM (empty string if the the object is naive).	(5)
#%Z	Time zone name (empty string if the object is naive).	 
#%%	A literal ''%'' character.
