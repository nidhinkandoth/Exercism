def acronym(phrase):
	words=phrase.split()
	acronym=''
	for i in words:
		acronym+=i[0]
	capital_acronym=acronym.upper()
	return capital_acronym

print acronym('Portable Network Graphics')
print acronym('Complementary metal-oxide semiconductor')
print acronym('First In, First Out')
print acronym('PHP: Hypertext Preprocessor')
