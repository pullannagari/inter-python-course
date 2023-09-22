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