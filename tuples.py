# Tuple: ordered, immutable, allows duplicate elements
# cannot be changed after its creation

tuple1 = ("Max", 28, "Boston") # created with paranthesis, they are optional
print(tuple1)

tuple2 = ("Max",)
print(tuple2)

# creating a tuple from an iterable
tuple3 = tuple(["hello", 1, "world"]) 
print(tuple3)

# accessing elements can be done with indexes
print(tuple1[0]) 
print(tuple1[-1])

# changing the elements
# cannot assign based on the index, for example the below code results in a n error
# tuple1[1] = 34 # TypeError: 'tuple' object does not support item assignment

# iterate over the elements in the tuple
for ele in tuple1:
    print(ele)

# check if something is present in tuple
if "Max" in tuple1:
    print("present!")

# get the number of elements in the tuple
print(len(tuple1))

# count the number of similar elemnts
print(tuple1.count("Max"))
print(tuple1.count("One"))

# reutrn the first occurrence of the element L to R
print(tuple1.index(28))
# print(tuple1.index("error")) # we face an index error

# convert to index
list1 = list(tuple1)
print(list1)

tuple3 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tuple3[2:5]) # last index is not inclusive
print(tuple3[2:]) # goes all the way to the end
print(tuple3[2::2]) # prints every second ele stating with the second index
print(tuple3[::-1]) # reverse the tuple

# unpacking the tuple
name, age, place = tuple1 # left side elements should match the number of elements to the right
name, *ele = tuple1 # work around to extract the first or last elements
print(name)
print(*ele) 

# list v/s tuple
# list takes more space compare to tuple
import sys
list2 = [0, 1, 2, "hello", True]
tuple4 = (0, 1, 2, "hello", True)
list_size = sys.getsizeof(list2,"bytes")
tuple_size = sys.getsizeof(tuple4, "bytes")
print(f"size of list is {list_size}, size of tuple is {tuple_size}")

# tuple is more efficient to iterate and create
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
