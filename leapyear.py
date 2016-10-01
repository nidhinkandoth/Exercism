year=int(raw_input("enter the year"))
if(year%400==0):
	print "%d is a leap year" %(year)
elif(year%100==0):
	print "%d is not a leap year" %(year)
elif(year%4==0):
	print "%d is a leap year" %(year)
else:
	print "%d is not a leap year" %(year)

 
