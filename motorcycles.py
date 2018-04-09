# modifying lists

motorcycles = ['yamaha', 'honda', 'bmw']
print(motorcycles)

motorcycles[0] = 'ktm'
print(motorcycles)

# adding elements at the end of a list using append 
motorcycles.append('ducati')
print(motorcycles)

# you can also build lists this way

motorcycles = []
motorcycles.append('honda')
motorcycles.append('BMW')
motorcycles.append('ktm')
print(motorcycles)

# insterting elements into a list

motorcycles = ['yamaha', 'honda', 'bmw']
motorcycles.insert(0,'ducati')
print(motorcycles)

# removing from a list using del statement 
del motorcycles[0]
print(motorcycles)

# can also use pop to remove last item on the list
# but it lets you work with the item afterwords

motorcycles = ['yamaha', 'honda', 'bmw']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print("The last motorcycle I owned was a " + 
		popped_motorcycle.title() + ".")
# Popping items from any position

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + 
	first_owned.title() + ".")

# Removing an item by value
motorcycles = ['yamaha', 'honda', 'bmw']
motorcycles.remove('yamaha')
print(motorcycles)
		
# cab also remove the variable
motorcycles = ['yamaha', 'honda', 'bmw', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too pricy.")


