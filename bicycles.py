# Lists
bicycles = ['trek', 'connondale', 'redline', 'specialized']
print(bicycles)

# accessing list
# first in list is always 0 in indexing 
# and you can use methods lile title

print(bicycles[0].title())

# can also get the last in the list by -1
print(bicycles[-1].upper())

# of course adding it all together 
message = "My first bike was a " + bicycles[0].title() + "."
print(message)
