# checking for inequality in statements

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	print("Hold the anchovies!")

# numerical comparisons
age = 25
print(age == 25) # will say true


# testing multiple conditions 
# you cant use an elif block or else it'll stop running
# so just use lots of if statements 

requested_toppings = ['mushrooms', 'extra cheese', 'green pepers']

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
	print('Adding pep')

# Checking for special items

requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry we are out of green peppers")
	else:
		print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")


# checking to see if something is blank
r_ts = []
if r_ts:
	for r_t in r_ts:
		print("Adding")
else:
	print("plain pizza?")


# using multi lists
requested_toppings = ['mushroom', 'extra cheese', 'green peppers']
available_toppings = ['mushroom', 'green peppers']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding" + requested_topping)
	else: 
		print("Topping unavailable")
		
print("finished your pizza!")

