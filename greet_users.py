# passing a list to a function

def greet_users(names):
	"""Pring a simple greeting to each user in the list"""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


