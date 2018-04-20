import datetime,math
today = datetime.date.today()
def getDate():
	someday=input('Enter a date(mm/dd/yyyy)')
	return someday
def validateDate(someday):
	try:
		[month, day, year] = map(int, someday.split('/'))
		oneday = datetime.date(year, month, day)
	except:
		print("Date not found/Check the Format")
		someday = getDate()
		oneday = validateDate(someday)
	return oneday 

#someday = datetime.date(2008, 12, 25)
someday = getDate()
day1 = validateDate(someday)
diff = day1 - today
total_days=(abs(diff.days))
print ("Difference is:"+"\n"+"Years="+str(int(total_days/365))+'\n')
print ("Months= {}\n".format((total_days/30)))
print ("Weeks= {}\n".format((total_days/7)))
print ("Days={}\n".format((total_days)))
print ("Seconds={}\n".format(((total_days*24*60*60))))