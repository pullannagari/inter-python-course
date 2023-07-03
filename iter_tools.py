# collection of tools for handling iterators 
# iterators are data types that can be used in loops
# advanced tools such as product, permutations, combinations, accumulate, groupby, and infinite iterators

# product
from itertools import product
# performs the cartesian product
a = [1, 2]
b = [3, 4]
prod = product(a, b) # performs the cartesian product
print(list(prod)) 

# permutations
from itertools import permutations
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))
perm = permutations(a, 2) # smaller lenght of permutations
print(list(perm))

#combinations
from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
comb = combinations(a,2)
print(list(comb))
comb_wr = combinations_with_replacement(a, 2) # combinations with repetitions allowed
print(list(comb_wr))

# accumulate
from itertools import accumulate
import operator
a = [1, 2, 3, 4]
acc = accumulate(a) # sum of elements until each index
print(list(acc))

acc_mul = accumulate(a, func=operator.mul) # multiply elements until each index
print(list(acc_mul))

max_list = [1, 2, 5, 3, 4]
acc_max = accumulate(max_list, func=max)
print(list(acc_max))

# groupby
from itertools import groupby
# groups the iter elements based on a function
def smaller_than_3(x):
    return x < 3

group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

# the same code could be written using lambda expression
group_obj = groupby(a, key=lambda x: x<3)
for key, value in group_obj:
    print(key, list(value))

persons = [{"name": "tim", "age": 24}, {"name":"Dan", "age": 24}, {"name": "lisa", "age":44}, {"name": "claire", "age": 28}]

group_by_age = groupby(persons, key=lambda x:x["age"])
for key, value in group_by_age:
    print(key, list(value))


#infinite iterators
from itertools import count, cycle, repeat

# count
for num in count(10): # creates an infinite counter with the starting vlaue as 10
    print(num)
    if (num == 100):
        break

# cycle
cycle_list = [1, 2, 3]
count = 0
for cyc_ele in cycle(cycle_list):
    print(cyc_ele)
    if cyc_ele == 1:
        count += 1
    if count == 5:
        break

# repeat
for rep_ele in repeat(10, 5): 
    # repeats 10, 5 times. repeats infinitely if second arg is not given
    print(rep_ele)
