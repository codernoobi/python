import datetime			#Import the datetime module and display the current date
x = datetime.datetime.now()
print(x)				#The date contains year, month, day, hour, minute, second, and microsecond.

print(x.year)
print(x.strftime("%A"))		#Return the year and name of weekday

x = datetime.datetime(2020, 5, 17)		#Create a date object
print(x)		

"""to create a date, we can use the datetime() class (constructor) of the datetime module.
The datetime() class requires three parameters to create a date: year, month, day."""

"""
The datetime() class also takes parameters for time and timezone 
(hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone)
"""

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))
"""
The datetime object has a method for formatting date objects into readable strings.
The method is called strftime(), and takes one parameter, format, to specify the format of the returned string
"""

"""
Directive	Description								Example
%a			Weekday, short version					Wed	
%A			Weekday, full version					Wednesday	
%w			Weekday as a number 0-6,0 is Sunday		3	
%d			Day of month 01-31						31	
%b			Month name, short version				Dec	
%B			Month name, full version				December	
%m			Month as a number 01-12					12	
%y			Year, short version, without century	18	
%Y			Year, full version						2018	
%H			Hour 00-23								17	
%I			Hour 00-12								05	
%p			AM/PM									PM	
%M			Minute 00-59							41	
%S			Second 00-59							08	
%f			Microsecond 000000-999999				548513	
%z			UTC offset								+0100	
%Z			Timezone								CST	
%j			Day number of year 001-366				365	
%U			Week number of year, Sunday as the first day of week, 00-53			52	
%W			Week number of year, Monday as the first day of week, 00-53			52	
%c			Local version of date and time										Mon Dec 31 17:41:00 2018	
%x			Local version of date					12/31/18	
%X			Local version of time					17:41:00	
%%			A % character							%
"""