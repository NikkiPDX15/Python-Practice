# Organizing a list

# using sort method for alphebetizing 
# this changes the list permanently 

cars = ['bmw', 'audi', 'toyota','mercedes']
cars.sort()
print(cars)

# can also reverse sort 
cars.sort(reverse=True)
print(cars)

# can also sort on a non permanent basis
# instead of a method we use a function 
cars = ['bmw', 'audi', 'toyota','mercedes']
print(sorted(cars))
print(cars)

# we can reverse the order of the list
cars = ['bmw', 'audi', 'toyota','mercedes']
cars.reverse()
print(cars)


# finding the length of a list
cars = ['bmw', 'audi', 'toyota','mercedes']
print(len(cars))




# if statements 
# this is a conditional test to check characters 
# the == is for an equality property 
# and is case sensitive

cars = ['bmw', 'audi', 'toyota','mercedes']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

# this is a conditional test to check characters 

car = 'Audi'
car.lower() == 'audi' # this would come up as true 



