# modifying a list in a afunction

# start with some designs that need to be printed

# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []


# # simulate printing each design until none are left
# # move each design to completed models after printing

# while unprinted_designs:
	# current_design = unprinted_designs.pop()
	# # simulate creating a 3D print from the design
	# print("Printing model: " + current_design)
	# completed_models.append(current_design)
	
	# # didsplay all completed models
	# print("\nThe following models have been printed:")
	# for completed_model in completed_models:
		# print(completed_models)

# # reorganize code and make more specific functions

def print_models(unprinted_designs, completed_models):
	"""
	Simulated printing each design until none are left
	Move each design to completed models after print
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		
		# simulate creating a 3D print from the design
		print("Printing model: " + current_design)
		completed_models.append(current_design)
		
def show_completed_models(completed_models):
	"""Show all models that were printed"""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_models)
		
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# if you want to not change a list, make it like below
print_models(unprinted_designs[:], completed_models)
# the slice notation makes a copy of list and sends it to function 
