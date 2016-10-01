def is_pangram(x):
	alphabets='abcdefghijklmnopqrstuvwxyz'
	if(len(x)<26):
		return False
	else:
		temp=list(alphabets)
		for i in x:
			if(i in temp):
				temp.remove(i)
	return (temp==[])

print is_pangram('the quick brown fox jumps over the lazy dog')
print is_pangram('the quick brown fish jumps over the lazy dog')
print is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog")
print is_pangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog")
