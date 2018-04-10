# dictionaries
# store info to a person/place/things
# collection of key value pairs 
# each key is connected to a value


alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# can also start with an empty dictionary

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# to change a value, just call the key

alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print('The alien is now ' + alien_0['color'] + ".")


# tracking position of an alien that can move at different speeds

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# Move the alien to the right
# determin how far to move the alien based on its current speed

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# this isthe fast alien
	X_increment = 3

# the new position is the old plus increment 
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))


# removing key value pairs
# remove the key
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
print(alien_0)
# using delete will permanently get rid of pairs 









