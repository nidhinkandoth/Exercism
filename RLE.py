def rle_encoder(x):
	i=0
	j=0
	count=0
	stack=[]
	ans=''
	while(i<len(x)):
		count=0
		while(j<len(x)):
			if(x[i]==x[j]):
				stack.append(x[i])
				j+=1
				

		ans+str(count)+x[i]
		i+=1

		
	return stack

print rle_encoder('AABBBCCCC')
