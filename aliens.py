# store a set of dictionaries in a list 
# or a list of items as a vlaue in a dictionary
# this is nesting :)

# list of dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print (alien)
	
	
	
# more than 3 aliens using range()
# empty list 
aliens = []

# make 30 aliens
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# make the first 3 yellow
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

# show first 5 aliens
for alien in aliens[:5]:
	print(alien)
print("...")

# show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))



