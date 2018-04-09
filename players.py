# working with part of a list

#slicing

players = ['charles', 'martina', 'michael' , 'florence', 'eli']
print(players[0:3])

# if you take out the start index, it just starts at beginning
print(players[:4])

# and if you take the end off, same concept 
# and can choose the last three with negative
print(players[2:])
print(players[-3:])


# looping through a slice

players = ['charles', 'martina', 'michael' , 'florence', 'eli']

print("Here are the first three players on my team: ")
for player in players[:3]:
	print(player.title())

# copying a list

my_foods = ['pizza', 'pad thai', 'sushi']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friend_foods)




