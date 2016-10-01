def series(x,n):
	s=''
	i=0
	result=[]
	while(i+n-1<len(x)):
		result.append(x[i:i+n])
		i+=1
	return result

print series('49142',3)
print series("97867564", 2)		
print series('123456789',2)		
