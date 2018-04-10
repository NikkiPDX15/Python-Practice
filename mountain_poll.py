# filling a dictionary with user input

# set a flag to indicate that polling is actve
responses = {}
polling_active = True

while polling_active:
	# prompt for persons name and response
	name = input("\nwhat is your name? ")
	response = input("\nWhich mountain would you like to climb? ")
	
	# Store response in directory
	responses[name] = response
	
	# find out if anyone else is going to take the poll
	repeat = input("Would you like to let another person respond? y/n ")
	if repeat == 'n':
		polling_active = False

# Polling is complete. show results
print("\n-----Poll Results-----")
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")
