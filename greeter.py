# writing clear prompts for inputs

# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

# prompt = "If you tell use who you are, we can personalize the messages you see."
# prompt += "\nwhat is your first name? "
# name = input(prompt)
# print("Hello, " + name + "!")

# # when we use the input() function python thinks that 
# # everything the user says is a string
# # so use int()

# age = input("How old are you? ")
# age = int(age)
# print(age)
# print(age>= 18) # true


# now we're into functions

# def greet_user(username): # function definition line 
	# """Display a simple greeting"""  # doc string to say what it is
	# print("Hello, " + username.title() + "!")
	
# greet_user('jesse')




def get_formated_name(first_name, last_name):
	""" Resturn a full name, neatly formatted"""
	full_name = first_name + ' ' + last_name
	return full_name.title()

while True:
	print("\nPlease tell me your name: ")
	print("Enter 'q' at any time to quit")
	
	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break
	
	formetted_name = get_formated_name(f_name, l_name)
	print("\nHello, " + formetted_name + "!")
	
	

