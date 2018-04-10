# while loops!!
# can use a while loop to count up through a series 
# of numbers

current_number = 1 
while current_number <=5:
	print(current_number)
	current_number +=1  # adds one to it 


# using continue while in a loop
# instead of breaking out of a loop you can
# continue to return to the beginning of the loop based
# on a result of a conditional test

# prints odd numbers 1-10

current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	
	print(current_number)


