# Approach 1:

import animal_module
import bird_module

animal_module.fly()   # Animal can't fly
animal_module.color() # Animal is black

bird_module.fly()  # Bird can fly
bird_module.color() # Bird is green

# Approach 2:

from animal_module import *
fly()
color()

from bird_module import *

fly()
color()


# Approach 3:

from animal_module import fly,color
fly()
color()

from bird_module import fly,color

fly()
color()




