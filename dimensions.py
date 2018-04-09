# tuples! lists that cannot be changed
# only real difference is the 90

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions: 
	print(dimension)
	
# you cant change the tuple on the outside, but assign it 
# another value on the inside to change it. 

dimensions = (200,50)
print(dimensions)
dimensions = (400,100)
print(dimensions)
