# For loops
# for loops are to apply something to every item in a list

magicians = ['alice','david','carolina']
for magician in magicians:
	print(magician)
#1 define list
#2 define variable in for loop for list
#3 tell it what to do

magicians = ['alice','david','carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I cant wait to see your next trick, " + magician.title()
		+ ".\n")
print("Thank you, everyone. That was a great magic show!")

# every indented line is in the loop
# anything on the outside will run after



