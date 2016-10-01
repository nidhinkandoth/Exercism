def sum_squares(n):
	Sum=(n*(n+1))/2
	return Sum**2

def squares_sum(n):
	ans=0
	for i in range(n+1):
		ans+=i**2
	return ans

def diff_square(n):
	return sum_squares(n)-squares_sum(n)

print diff_square(10)
print diff_square(100)
