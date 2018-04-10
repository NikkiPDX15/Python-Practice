# working with classes
# # object - orientd programming

# create a class and make objects from a class is called an instance
# what kind of info that can be stored in those instances

# aka my class is a dog, and this is who the dog is and what it does
# then import dog every time your program has a dog

# a function that is part of a class is a method
# init is a method that runs auttomatically whenever we create a 
# new instance based on the Dog Class

class Dog():
	""" A simple attempt to model a dog """
	def __init__(self, name, age):
		"""Initialize name and age attributes"""
		self.name = name
		self.age = age
	# any variable with prefix self is available all methods in class
	# these are called attributes
	
	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(self.name.title() + " is now sitting.")
	
	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + " rolled over!")


my_dog = Dog('bailey', 13)
print("\nMy dog's name is " + my_dog.name.title() + ".")
print("\nMy dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

# can apply to multi instances and use the methods 
your_dog = Dog('louie', 11)
your_dog.sit()
your_dog.roll_over()
