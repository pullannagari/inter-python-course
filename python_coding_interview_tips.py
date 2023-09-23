# easier and concise 
# dynamically typed language (so variables can be reassigned to different types)
n = 0
print('n= ', n)
n = "abc"
print('n= ', n)

# multiple assignments
n, m  = 0, "abc"

# incrementing
n = n + 1
n += 1
# cannot do n++

# None is null (abscence of value)
n = None
print('n= ', n)
n = 4
print('n= ', n)

# if statements don't need parantheses or curly braces
# indentation is used
n = 1
if n > 2:
    n -= 1
elif n == 1:
    n *= 2
print('n= ', n)

# paranthesis needed for multi-line conditions
# and = &&
# or = ||
n, m = 1, 2
if n > 0 and m > 1:
    print('n= ', n)
# multi-line
if (n>0 or m > 0
    and m > n):
    print('n= ', n)

# while loop
n = 0
while n < 5:
    print('n= ', n)
    n += 1

# for loop using range
# range produces a sequence of integers from 
# start (inclusive) to stop (exclusive) by step
for i in range(5):
    print(i)

for i in range(2, 5):
    print(i)

# for printing in reverse
# 1 is not inclusive, so won't be printed
for i in range(5, 1, -1):
    print(i)

# division
print(5/2) # gives floating result 2.5
print(5//2) # gives int result 2 (floor)

# CAREFUL: most languages round towards 0 by default
# python rounds to floor for negative numbes too
print(-3//2) # gives -2 not -1 unlike other programming languages
# to work around, you need to convert the result to integer
print(int(-3/2)) # -1.5 will be converted to int and -1 will be the result

# modding is similar to most languages, except for negative values
print(10%3) # results 1
print(-10%3) # results 2, expected is -1
# to work around, you need to use the math module
import math
print(math.fmod(-10, 3)) # modd according to c platform

#few math helpers
print(math.floor(3 / 2))
print(math.ceil(3 / 2))
print(math.sqrt(2))
print(math.pow(2,3))

# Max/Min Int
# python numbers are infinite, no overflowing
inf = float("inf") # positive infinity
ninf = float("-inf") # negative infinity
very_large_num = math.pow(2,300)
if very_large_num < inf:
    print("infinity is ", inf)

# Arrays are called lists in python
arr = [1, 2, 3]
print(arr)
# lists are dynamic in python, 
# they can be used as stacks
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

# inserting into a specific index, linear time operation
arr.insert(1, 7)
# assignment is not linear time operation
arr[1] = 5
print(arr)

# initializing arr of size n with default value of 1
n = 5
arr_ones = [1] * n
print(arr_ones)
print(len(arr_ones))
# you can initialize with negative values too
arr_nones = [-1] * n
print(arr_nones)
# you can initialize arr of arrays
# CAREFUL: THE BELOW OPETATION WILL REPEAT THE SAME LIST 4 TIMES
arr_arr  = [[-1]*4]*4 
print(arr_arr)
# MORE CONCISE WAY OF DOING THIS IS
arr_arr = [[0]*4 for i in range(4)]
print(arr_arr)

# -1 index gives the last element
# -2 index gives the penultimate element
arr = [0, 1, 2, 3, 4, 5]
print(arr[-1])
print(arr[-2])

# slicing the lists, most useful feature sin python
print(arr[1:3]) # index 3 is exclusive
print(arr[::-1]) # reverse of the array
print(arr[4:2:-1]) # index 4 and 3
print(arr[4:2:-2]) # index 4

# unpacking
# number of variables match the elements in the list 
a, b, c = [1, 2, 3]
print(a, b, c)
# super useful when we want to go over a list of pairs
a, b, c = [(1,2), (2,4), (-3,3)]
print(a, b, c)

# loop throught the arrays
# using index
for i in range(len(arr)):
    print(i)

# without index
for num in arr:
    print(num)

# with enumerate function
for i, n in enumerate(arr):
    print(i, n)

# looping through multiple arrays simultaneously
arr_1 = ["a", "b", "c", "d"]
arr_2 = [1,2,3,4,5]
# zip combines them in pairs, unpack 
for a1, a2, a3 in zip(arr_1, arr_2, range(11,15)): 
    print(a1, a2, a3) # doesn't print 5 or 15, picks the shortest arr as max


# reverse an array
arr_1.reverse()
print(arr_1) # reverses the actual array in-place
print(arr_2[::-1]) # doesn't change the actual array

# sorting an array
arr_sort = [5, 4, 2, 7, 9, 8]
arr_sort.sort() # sorts the actual array, in ascending order by default
print(arr_sort)
arr_sort.sort(reverse=True) # sort in descending order
print(arr_sort)

# we can sort the list of stirings too
arr_sort_strings = ["danny", "boddy", "grit", "len", "mars", "alice"]
arr_sort_strings.sort()
print(arr_sort_strings) # by default sorts in alphabetical order

# to sort base on custom param(len for ex.)
arr_sort_strings.sort(key=lambda x: len(x), reverse=True)
print(arr_sort_strings)

# list comprehension
arr = [i+i for i in range(5)]
print(arr)

arr_arr = [[0]*4 for i in range(4)]
print(arr_arr)


# strings are similar to arrays
s = "abc"
print(s[0:2]) # prints ab

# but they are immutable
# so the below will create a new string
# any string update operation is O(N) time operation
s += "def"
print(s)

# valid numeric strings can be converted
print(int("123")+1)
# and numbers can be converted to strings
print(str(123) + str(1))

# to get an ascii value of a character, use ord()
print(ord("a"))
print(ord("A"))

# joining a list of strings with a delimeter
strings = ["ab", "cd", "ef"]
print("".join(strings)) # joining with empty string delimeter


# Queues in python are double ended queues, hence name deque
from collections import deque

queue = deque()
queue.append(1)
queue.append(2) # O(1) time
queue.append(3)
print(queue)

queue.popleft() # O(1) time
print(queue)

queue.appendleft(1) # O(1) time
print(queue)

queue.pop() # O(1) time
print(queue)


# HashSet or set in python
# search and insert elements in O(1) time
# no duplicates
seta = set()

seta.add(1)
seta.add(2)
seta.add(1)
print(seta)
print(len(seta))
print(1 in seta) # check if key exists using in
print(3 in seta)

seta.remove(1) # O(1) time
print(1 in seta)

# list to set
print(set([1, 2, 3, 3]))
# set comprehension
setb = {i for i in range(5)}
print(setb)


# hashmap or dict in python
# key value pair, no duplicate keys
mapa = {}
mapa["alice"] = 88
mapa["bob"] = 77
mapa["cat"] = 70
print(mapa)
print(len(mapa)) # prints number of keys
mapa["alice"] = 80 # reassignment/modification
print("alice" in mapa) # check if key exists
mapa.pop("alice") # pop the key, value pair matching key
print("alice" in mapa)
# another way to delete the key, value
print("bob" in mapa)
del mapa["bob"]
print("bob" in mapa)

mapb = {"alice": 1, "bob": 2} # another way of creating map
print(mapb)

# dict comprehension
map_comp = {i : 2*i for i in range(3)} # useful to create graph adjacency list
print(map_comp)
for key in mapb:
    print(key, mapb[key])

for val in map_comp.values(): # directly iterate through values
    print(val)

for key, val in mapb.items(): # using unpacking
    print(key, val)


# Tuples are like arrays but immutable
# similar to lists, we use paranthesis instead of brackets
tup = (1, 2, 3)
print(tup)
print(tup[0])
print(tup[-1])
# can't modify
# tup[0] = 0

# you'll mostly use tuples as keys to hash maps or hash set in interviews
tup_map = { (1,2): "three"}
print(tup_map[(1,2)])

tup_set = set()
tup_set.add((1,2))
# lists are not hashable, so can't be used as keys, so we use tuples
print((1,2) in tup_set) 


# Heaps are used to find min, max of a set a values
# under the hood are arrays
# by default the heap in python is min heap

import heapq

minhp = []
heapq.heappush(minhp, 3)
heapq.heappush(minhp, 2)
heapq.heappush(minhp, 5)
heapq.heappush(minhp, 1)
# minimum value is always at index 0
print(minhp[0])

while len(minhp):
    print(heapq.heappop(minhp))

# no max heap in python
# workaround is to use min heap and mutiply by -1 when push & pop
maxhp = []
heapq.heappush(maxhp, -3)
heapq.heappush(maxhp, -2)
heapq.heappush(maxhp, -5)
heapq.heappush(maxhp, -1)
# max value then is
print(-1 * maxhp[0])

while len(maxhp):
    print(-1 * heapq.heappop(maxhp))

# build heap from initial values
max_heap_init = [2, 1, 8, 4, 5]
heapq.heapify(max_heap_init)
while max_heap_init:
    print(heapq.heappop(max_heap_init))

# functions
def my_func(n, m):
    return n * m

print(my_func(8, 8))
# nested functions are most useful in coding interviews
# very helpful in recursive functions
def outer(a, b):
    c = 30

    def inner():
        # access to a, b, c without passing them to inner func
            return a + b + c
    
    return inner()
    
print(outer(10, 20))

# nested functions can modify objects, but not reassign values
# unless using nonlocal keyword
def double(arr, val):
    def helper():
        # modifying array works, updated the original array
        for i , n in enumerate(arr):
            arr[i] *= 2
        # will only modify val inside helper scope
        # val *= 2

        # to update the in outside helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr)
    print(val)

double([1]*4, 3)


# Class
# more concise, but limited
class MyClass:
    # __init__ is the name constuctor
    def __init__(self, nums) -> None:
        # self is like this keyword in other languages
        # to create member variables we can use self.var_name
        self.nums = nums
        self.size = len(nums)

    # self needs to be passed to evey member function of the class
    def get_length(self):
        return self.size
    
    def get_double_length(self):
        return 2 * self.get_double_length()
    


        

