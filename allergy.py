#Converting to binary made the problem easy, and anding with the number could easily identify the components

def allergy(n):
		
	result="The person is allergetic to the following:\n"
	if((n&1)==1):
                result+='eggs\n'
	if((n&2)==2):
		result+='peanuts\n'
	if((n&4)==4):
		result+='shellfish\n'
	if((n&8)==8):
                result+='strawberries\n'
	if((n&16)==16):
                result+='tomatoes\n'
	if((n&32)==32):
                result+='chocolate\n'
	if((n&64)==64):
                result+='pollen\n'
	if((n&128)==128):
                result+='cats\n'
	return result

print allergy(255)
print allergy(34)
