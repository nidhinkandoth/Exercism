def isprime(x):
	if(x>0):
		flag=True
		for i in range(2,x):
			if((x%i)==0):
				flag=False
		return flag
			
	else:
		return False	

def nth_prime(n):
	count=0
	i=0
	while(count<n+1):
		if(isprime(i)):
			count+=1
		i+=1
	return i-1

print nth_prime(6)
		


			
				
		
