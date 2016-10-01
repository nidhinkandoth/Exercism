class Triangles():
	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
	def kind(self):
		if(self.a==self.b==self.c):
			return "equilateral"
		elif(self.a==self.b or self.a==self.c or self.b==self.c):
                        return "isosceles"
		else:
			return "scalene"
	def legal(self):
		return (self.a+self.b>self.c and self.a+self.c>self.b and self.b+self.c>self.a)


sides=raw_input("enter side lengths")
y=sides.split()

ex=Triangles(int(y[0]), int(y[1]), int(y[2]))
if(ex.legal()):
	print ex.kind()
else:
	print "Invalid"		
