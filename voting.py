# if statements 
# if condition test
	# do something 
	
age = 19
if age >= 19:
	print("you are old enough to vote!")
	print("Have you registered yet?")

# if else statements 

age = 17

if age>= 18:
	print("you are old enough to vote!")
	print("Have you registered yet?")
else:
	print("Sorry you can't vote")

# if else chain

age = 12

if age < 4:
	print("your admission is free")
elif age < 18:
	print("your admission is $5")
else:
	print("your admission is $10")

# simplified

age = 25
if age <4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10
print("your admission is $" + str(price) + ".")

# if you just want to use elifs you can. no need for an 
# else if you dont need it 



