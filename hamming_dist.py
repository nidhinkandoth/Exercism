def hamming_dist(a,b):
	count=0
	i=0
	if(len(a)!=len(b)):
		print("Not possible to calculate hamming distance")
	else:
		while(i<len(a)):
			if(a[i]!=b[i]):
				count+=1
			i+=1
	return count

print hamming_dist('GATACA', 'GCATAA')
print hamming_dist('GGACGGATTCTG', 'AGGACGGATTCT')
