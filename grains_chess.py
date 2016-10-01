def on_square(n):
	return 2**(n-1)

def total_after(n):
	total=0
	for i in range(n):
		total+=(2**i)
	return total

print on_square(32)
print total_after(32)	
