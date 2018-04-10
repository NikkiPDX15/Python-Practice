# removing all instances of a specific value from list

pets = ['dog', 'cat', 'goldfish', 'cat', 'rabbit']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
print(pets)

# passing arguments for functions
# there are key arguments and positional

# this positional one has to be called in order 

def describe_pet(animal_type, pet_name):
	"""Display info on pet"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# this positional one has to be called in order 
describe_pet('hamster','harry')
describe_pet('dog', 'willie')

# or call it like this
describe_pet( animal_type = 'cat', pet_name = 'lu lu')

# can also set a defualt 
# goes to default unless called with specific value

def describe_pet(pet_name, animal_type = 'dog'):
	"""Display info on pet"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name = 'willie')

# if you set a default, it has to be last since it doesnt 
# have to be inputed 

