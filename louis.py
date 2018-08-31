# louis.py

class Animal(object):
	def __init__(self, legs, name):
		self.legs = legs
		self.name = name
		
	def sleep(self, hours):
		if hours == 1:
			hr = "hour"
		else:
			hr = "hours"
		print "%s is sleeping for %d %s!" % (self.name, hours, hr)
			
class Dog(Animal):
	def __init__(self, name):
		self.name = name
		self.legs = 4

	def bark(self):
		print "%s just harfed! How cute!" % self.name

	def bark(self, number):
		barkStr = "Harf! " * number
		print "%s just harfed %d times! %s" % (self.name, number, barkStr)

IntroString = "Please enter your dog's name or q to quit "
PetName = raw_input("%s" % IntroString)

if PetName.lower() == "q" or PetName.lower() == "quit":
	print "See ya"
	exit()
else:
	louis = Dog(PetName)
	#louis.bark() # paramater error
	louis.bark(3) 
	louis.sleep(1)
