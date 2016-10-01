class Space_age():
	def __init__(self,seconds):
		self.seconds=seconds

	def on_earth(self):
		one_year=31557600
		age=self.seconds/one_year
		return age
	def on_mercury(self):
		one_year=0.2408467*31557600
		return self.seconds/one_year
	def on_venus(self):
		return self.seconds/0.615197260*31557600
	def on_mars(self):
		return self.seconds/1.8808158*31557600
	def on_jupiter(self):
		return self.seconds/11.862615*31557600
	def on_saturn(self):
		return self.seconds/29.447498*31557600
	def on_uranus(self):
		return self.seconds/84.016846*31557600
	def on_neptune(self):
		return self.seconds/164.79132*31557600
	
age=Space_age(1000000000)
print age.on_earth()
print age.on_venus()
age = Space_age(2134835688)
print age.on_mercury()

