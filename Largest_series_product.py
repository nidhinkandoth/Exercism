def Largest_s_product(sequence,n):
	splitted_into_n=[]
	i=0
	while(i+n-1<len(sequence)):
		splitted_into_n.append(sequence[i:i+n])
		i+=1
	Largest=0
	product=1
	for i in splitted_into_n:
		product=1
		for j in i:
			product*=int(j)
		if(product>Largest):
			Largest=product
	return Largest


print Largest_s_product("0123456789", 2)
print Largest_s_product("1027839564", 3)
