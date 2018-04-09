# make squares of numbers
# ** is to the power of 

squares = []

for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)


# for a more concisely written code

squares = []

for value in range(1,11):
	squares.append(value**2)
print(squares)

# simple stats

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))


# try list comprehension ie only using one line of code

squares = [value**2 for value in range(1,11)]
print(squares) 






