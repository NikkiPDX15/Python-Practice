# inheriting traits between classes
# instead of coding from scratch

# now we create a child class. the parent class must be in same file
# and appear before the child class

class Car():
	"""A simple attempt to represent a car."""
	
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car. """
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0  # defaults not included in parameters
		
	def get_descriptive_name(self):
		"""Return a neatly formatted name"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		""" Print a statement showing the car's mileage"""
		print("This car has " + str(self.odometer_reading) +
			" miles on it.")
	
	def update_odometer(self, mileage): # modify attributes in method
		"""
		Set odometer reading to given value.
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >- self.odometer_reading:
			self.odometer_reading = mileage	
		else:
			print("You can't roll back an odometer!")
	
	# incremementing an attributes value through a method
	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading"""
		self.odometer_reading += miles
		

class Battery():
	"""A simple attempt to model a battery for an electic car."""
	def __init__(self, battery_size = 70):
		"""Initialize the battery's attributes"""
		self.battery_size = battery_size
	
	def describe_battery(self):
		"""Print a statement describing the battery size"""
		print("This car has a " + str(self.battery_size)+ "-kWh battery.")
	
	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 83:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)

class ElectricCar(Car):
	"""Represents aspects of a car, specific to electric vehicles"""
	def __init__(self, make, model, year):
		"""
		Initialize attribites of the parrent class.
		The initialize attribites specific to an electric car 
		"""
		super().__init__(make, model, year) # connects with parent
		self.battery = Battery()
			
	# overiding methods from parent class
	def fill_gas_tank(self):
		"""Electric cars dont have gas tanks"""
		print("This car doesn't need a gas tank!")
###

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()



# making instances as attributes
# lets look at the electric car battery

