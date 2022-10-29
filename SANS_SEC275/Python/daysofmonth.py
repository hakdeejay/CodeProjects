### Print date, day and activity.

Monday = {
	'Day': 'Mon',	
	'Activity': 'Swimming'
          }

Tuesday = {
	'Day': 'Tue',	
	'Activity': 'SANS Study'
          }

Wednesday = {
	'Day': 'Wed',	
	'Activity': 'BookClub'
          }

Thursday = {
	'Day': 'Thu',	
	'Activity': 'SANS Study'
          }
Friday = { 
	'Day': 'Fri',	
	'Activity': 'D&D'
	}
Saturday = {
	'Day': 'Sat',	
	'Activity': 'SANS Study'
	}
Sunday = {
	'Day': 'Sun',	
	'Activity': 'Rest'
	}

month = 'July'
week = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]
dayMonth = 1 #count the days of the month
start = 4 #ensures we start on the correct day of the week
end = start + 31 #this is to ensure we print 31 days for july

def dayOfWeek(day):
	global dayMonth # to access the global dayMonth variable
	print(str(dayMonth)+'\t',end='') #print day of month, a tab, the 'end' to stay on same line
	print(week[day%7].get("Day"),week[day%7].get("Activity")) #syntax to access dictionary
	dayMonth += 1

for weekDay in range(start,end):
	dayOfWeek(weekDay)