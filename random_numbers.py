# python comes with different built in modules for random number generation


# random module - pseudo random numbers
# Because these numbers are reproducible, don't use for security purposes
import random

# pseudo random numbers for different distribution
# can be reproduced 
random1 = random.random()
print(random1) # float random in the range 0 - 1 
random1 = random.uniform(1, 10)
print(random1) # random float in the spedified range
random1 = random.randint(1, 10)
print(random1) # random int int he range including the upper bound
# to exclude the upper bound
random1 = random.randrange(1, 10)
print(random1)

# random variate func, for statistics
random1 = random.normalvariate(0, 1) # mu , sigma params
# picks a random value from normal distribution with a mean of 0 and a standard deviation of 1
print(random1)

# different function to work with sequences
list1 = list("abcdefgh")
print(list1)

# pick a random choice
ele1 = random.choice(list1)
print(ele1) # picks a random element from the list

# pick more elements
elements = random.sample(list1, 3)
print(elements)

# to pick elements more than once
rep_elements = random.choices(list1, k=3)
print(rep_elements)

# to shuffle the list
random.shuffle(list1) # shuffles the list in place
print(list1)

# seeding will preserve the random picks
random.seed(1)
print(random.random())
print(random.randint(1,10))

random.seed(2)
print(random.random())
print(random.randint(1,10))

# exaclty same number as for seed 1
random.seed(1)
print(random.random())
print(random.randint(1,10))

# exaclty same number as for seed 2
random.seed(2)
print(random.random())
print(random.randint(1,10))

# use secrets for security purposes
# takes more time for the algorithms - pitfall

import secrets

sec1 = secrets.randbelow(10)
print(sec1) # upper bound not included

sec1 = secrets.randbits(4) # random value till 15 which is 1111
# 1010
print(sec1)

sec_choice = secrets.choice(list1) # produces a choice which is not reproducible
print(sec_choice)


# working with arrays/lists, use numpy 
import numpy as np

float_list = np.random.rand(3) # produces 3 random floats
print(float_list)

int_list = np.random.randint(0, 10, (3, 4)) # 10 is excluded
print(int_list)

arr = [[9, 2, 6 ,7], [0, 0, 9, 5], [0, 9, 6, 8]]
print(arr)
np.random.shuffle(arr) # only x-axis is shuffled, doesn't shuffle the elements with in the nested arrays
print(arr) 

# the seed function is different from built in random
np.random.seed(1)
print(np.random.rand(3,3))

# the seed function is different from built in random
np.random.seed(1)
print(np.random.rand(3,3))