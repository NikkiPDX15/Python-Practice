# importing entire module from pizza.py

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'sausage', 'onion')

# to call it, import the .py
# then use module_name.function_name()

# can also import specific functions instead of whole page

from pizza import make_pizza
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms', 'green peppers', 'extra cheese')

# can also make an alias for mod

import pizza as p

p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushrooms', 'green peppers', 'extra cheese')

# or importing all function in a module

from pizza import *

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms', 'green peppers', 'extra cheese')
