# Returning a simple value using functions

def get_formated_name(first_name, last_name):
	"""Return a full name, neatly formatted"""
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formated_name('jimi','hendrix')
print(musician)

# making an arguement optional

def get_formated_name(first_name, middle_name, last_name):
	"""Return a full name, neatly formatted"""
	full_name = first_name + ' ' + middle_name + ' ' + last_name
	return full_name.title()

musician = get_formated_name('john', 'lee','hooker')
print(musician)


# now make middle name optional
def get_formated_name(first_name, last_name, middle_name = ''):
	"""Return a full name, neatly formatted"""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formated_name('john', 'lee','hooker')
print(musician)

musician = get_formated_name('jimi','hendrix')
print(musician)
