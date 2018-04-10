# modulo operator (%) divides one number by another and 
# then returns the remainder

# when one number is divisable by another
# the remainder is 0 so the modulo operator is always 0

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nthe number " + str(number) + " is odd.")
	
	
