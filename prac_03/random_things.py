"""Write 3 different versions of code to generate random Boolean (True or False)"""

# 1
import random

random_number = (random.randint(1, 2))
if random_number == 1:
    result = True
else:
    result = False

# 2
random_number = (random.randint(1, 100))
if random_number % 2 == 0:
    result = True
else:
    result = False


# 3
random_boolean = (random.randint(True, False))
