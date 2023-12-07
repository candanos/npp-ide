from datetime import date 
from datetime import time 
from datetime import timedelta 
from datetime import datetime

# Get today's date 
today = date.today() 
print("Today is: ", today) 
print("Date components:")
print("year:" + str(today.year)) # class variables are integer.
print("month:" + str(today.month))
print("day:" + str(today.day))
print("day of week" + str(today.weekday()) ) # weekday is a function. Monday is 0
  
# Yesterday date 
yesterday = today - timedelta(days = 1) 
print("Yesterday was: ", yesterday) 
now = datetime.now()
print("Now is: " + str(now))

#Formatting with str-f-time: 
print(datetime.now().strftime("%H:%M:%S")) 
print(datetime.now().strftime("%H : %M"))
print(datetime.now().strftime("%H-%M"))

#Presets:
# Date
# %m/%d/%Y 	06/05/2013
# %A, %B %e, %Y 	Sunday, June 5, 2013
# %b %e %a 	Jun 5 Sun
# Time
# %H:%M 	23:05
# %I:%M %p 	11:05 PM

# Time:
# %l 	1 	Hour
# %H 	00..23 	24h Hour
# %I 	01..12 	12h Hour
# %M 	00..59 	Minute
# %S 	00..60 	Second
# %p 	AM 	AM or PM
# %Z 	+08 	Time zone
# %j 	001..366 	Day of the year
# %% 	% 	Literal % character

# Date:
# %a 	Sun 	Weekday
# %A 	Sunday 	 
# %w 	0..6 (Sunday is 0) 	 
# %y 	13 	Year
# %Y 	2013 	 
# %b 	Jan 	Month
# %B 	January 	 
# %m 	01..12 	 
# %d 	01..31 	Day
# %e 	1..31 	 