# can see if two numbers are not equal

answer = 17
if answer != 42:
	print("That is not the correct answer. Please try again!")

# check multiple conditions using and 
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21) # this comes out false

print(age_0 >= 21 or age_1 >= 21) # true

# check to see if a value is in a list

check = ['two', 'one', 'three']
print('two' in check) # true
