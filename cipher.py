def cipher(x):
	alpha='abcdefghijklmnopqrstuvwxyz'
	cipher_code=''
	for i in x:
	        cipher_code+=str(alpha[-(alpha.index(i)+1)])
		#print i
		#print (alpha[-(alpha.index(i)+1)])
	return (cipher_code)

print cipher('abc')
print cipher('xyz')

