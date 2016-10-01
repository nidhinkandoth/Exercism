def rna_trans(x):
	ans=''
	for i in x:
		if(i=='G'):
			ans=ans+'C'
		elif(i=='C'):
			ans=ans+'G'
		elif(i=='T'):
			ans=ans+'A'
		elif(i=='A'):
			ans=ans+'U'
	return ans
			

print rna_trans('ACGTGGTCTTAA')
