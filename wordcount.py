def word_count(x):
	word=x.split()
	ans=[]
	for i in word:
		ans.append(word.count(i))
	return ans

print word_count("a b c d")
print word_count("a b c d e f")
print word_count("a b c d e f g h")
		
