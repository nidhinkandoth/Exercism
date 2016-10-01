def scrabble_score(x):
	scores={('A', 'E', 'I', 'O','U', 'L','N', 'R', 'S', 'T'):1,('D', 'G'):2,('B','C','M','P'):3,('F','H','V','W','Y'):4,'K':5,('J','X'):8,('Q','Z'):10}
	score=0
	for i in x.upper():
		for j in scores.keys():
			if(i in j):
				score+=scores.get(j)
	return score

print scrabble_score("quirky")
print scrabble_score("OxyphenButazone")				
