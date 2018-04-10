# dictionaries can be used for polling 

favorite_languages = {
	'jen': 'python',
	'paul': 'solid works',
	'nikki': 'RStudio',
	}
print("Paul's favorite language is " + 
	favorite_languages['paul'].title() + ".")
	

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + 
		language.title() + ".")
		
# looping through all keys in a dictionary 
# use keys() method

for name in favorite_languages.keys():
	print(name.title())
	
	
# look at name matching 

favorite_languages = {
	'jen': 'python',
	'paul': 'solid works',
	'nikki': 'RStudio',
	}

friends = ['phil', 'jen']
for name in favorite_languages.keys():
	print(name.title())
	
	if name in friends:
		print("Hi " + name.title() + 
		", I see your favorite language is " + 
		favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")
	
# looping through keys in order

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")
	
# looping through values

print("the following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())
	
# can also use set() to bring back unique values only

print("the following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())


# can nest a list inside a dictionary any time

favorite_languages = {
	'jen': ['python', 'ruby'],
	'paul': ['solid works', 'CAD'],
	'nikki': ['RStudio', 'python'],
	}

for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())



