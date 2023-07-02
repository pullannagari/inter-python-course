# sets: unordered, mutable, no duplicates
set1 = {1, "hello", 3}
print(set1)

set2 = set([1, 2, 3, 5, "hey", "hello"]) # another way of creating a set
print(set2)

set3 = set("hello")
print(set3) # order is arbitary, also only one l appears

# you can create an empty set as below
set4 = set()
set4.add(1)
set4.add(3)
set4.add(7)
print(set4)

set4.remove(3) # removes the element, raises an exception if the element doesn't exist
print(set4)

set4.discard(5) # doesn't raise an error if the element is not found in the set
set4.pop() # pops an arbitary value from the set

set4.clear() # clears the whole set

for ele in set1:
    print(ele) # iterate through the set

if 3 in set1:
    print("element in the set")

# unions and intersection
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

un = odds.union(evens)
print(un)

int = odds.intersection(evens)
print(int) # returns an empty set

prime_odd = odds.intersection(primes)
print(prime_odd) # odd prime numbers

prime_even = evens.intersection(primes)
print(prime_even) # even prime numbers

# diff of sets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

print(setA.difference(setB)) # get the elements from 4-9
print(setB.difference(setA)) # get the elemtns 10-12


# symmetric difference method
print(setA.symmetric_difference(setB)) # get the elements 4-9 and 10-12
print(setB.symmetric_difference(setA)) # same as above


setA_copy = set(setA)
setA_copy1 = set(setA)

# above set operations return new set
# to update the sets in place
setA.intersection_update(setB)
print(setA) # updates the set with only matching values

setA_copy.difference_update(setB)
print(setA_copy) # updates with unique values from both the sets

setA_copy1.symmetric_difference_update(setB)
print(setA_copy1) # elements mutually exclusive from both the sets
print(setA_copy1)

setA.update(setB)
print(setA) # updates the setA and setB with unique values

subsup1 = {1, 2, 3, 4, 5, 6}
subsup2 = {1, 2, 3}
print(subsup1.issuperset(subsup2))
print(subsup2.issuperset(subsup1))
print(subsup1.issubset(subsup2))
print(subsup2.issubset(subsup1))
print(subsup1.isdisjoint(subsup2)) # True if there is no intersection

# frozen set is a set which is immutable, has all the properties of a set
frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set)
