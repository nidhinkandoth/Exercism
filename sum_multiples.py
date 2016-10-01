def sum_multiples(n,x):
	Sum=0
	multiples=[]
	Set_of_multiples=set
	for number in range(n):
		for i in x:
			if(number%i==0):
				multiples.append(number)
	Set_of_multiples=set(multiples)
	for i in Set_of_multiples:
		Sum+=i

	return Sum

print sum_multiples(20,[3,5])
print sum_multiples(150, [5, 6, 8])

print sum_multiples(10000, [43, 47])
