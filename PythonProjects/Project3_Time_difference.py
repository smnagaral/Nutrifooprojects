from time import strftime
import math
#print (int(strftime("%Y-%m-%d %H:%M:%S")))

Y1=int(strftime("%Y"))
m1=int(strftime("%m"))
d1=int(strftime("%d"))
H1=int(strftime("%H"))
M1=int(strftime("%M"))
S1=int(strftime("%S"))

date=input('Enter a date(mm/dd/yyyy)')
replace=date.replace('/',' ')
convert=replace.split()
month=convert[0]
day=convert[1]
year=convert[2]

Y2=int(year)
m2=int(month)
d2=int(day)
H2=0
M2=0
S2=0

while ((Y2>Y1) or (m2>12) or (d2>30)):
	print("Invalid Date \n")
	date=input('Please enter correct date(mm/dd/yyyy)')
	replace=date.replace('/',' ')
	convert=replace.split()
	month=convert[0]
	day=convert[1]
	year=convert[2]

	Y2=int(year)
	m2=int(month)
	d2=int(day)
	H2=0
	M2=0
	S2=0

total_days = ((abs(Y2-Y1))*365)
if m2 > m1:
	total_days -=365
	months_difference = 12-(abs(m2-m1))
	total_days += (months_difference*30)
	if d2 > d1:
		total_days -=30
		total_days += (30-(abs(d2-d1)))
	else:
		total_days += abs(d1-d2)
else:
	total_days += (abs(m1-m2))*30
	if d2 > d1:
		total_days -=30
		total_days += (30-(abs(d2-d1)))
	else:
		total_days += abs(d1-d2)

print ("Difference is:"+"\n"+"Years="+str(int(total_days/365))+'\n')
print ("Months= {}\n".format((total_days/30)))
print ("Weeks= {}\n".format((total_days/7)))
print ("Days={}\n".format((total_days)))
print ("Seconds={}\n".format(((total_days*24*60*60)+S1)))

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# Issues:

# No functions here again
# Lines 12 - 17 can be optimized to make it one line
# Input is not sanitized
# Same issues as Project1
# Program takes any number (0, -21, -447493)
# Please refer Project1's comments section for additional information

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
