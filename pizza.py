# store information about pizza being ordered
# # put a list in a dictionary

# pizza = {
	# 'crust': 'thick',
	# 'toppings': ['mushrooms', 'extra cheese'],
	# }
# # summarize order
# print(" You ordered a " + pizza['crust'] + "-crust pizza " + 
	# "with the following toppings:")
# for topping in pizza['toppings']:
	# print("\t" + topping)


# # passing arbitrary number of arguments 
# # aka you dont know how many arguments you'll need to accept 


# # the * makes an empty tuple called that name and pack whatever
# # values it receives into this tuple

# # arbitrary must be places last for multiple kinds of arguments
# # that way it only grabs one value then places the rest in the other
# # category

# def make_pizza(size, *toppings):
	# """Summarize pizza. """
	# print("\nMaking a " + str(size) + 
		# "-inch pizza with the following toppings:")
	# for topping in toppings:
		# print("- " + topping)
	
# make_pizza(16,'pepperoni')
# make_pizza(12,'mushrooms', 'green peppers', 'extra cheese')

# importng an entire function

def make_pizza(size, *toppings):
	"""Summarize pizza. """
	print("\nMaking a " + str(size) + 
		"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)
	

