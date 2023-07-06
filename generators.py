# generators are functions that return an object that can be iterated over
# speciality is they can generate the object lazily, meaning only one at a time only when asked for it
# much more memory efficient compared to other sequence objects when dealing with large objects

# defined similar to function, but with a yield keyword instead of return keyword
def generator1():
    print('before 1st yield')
    yield 1
    print('before 2nd yield')
    yield 2
    print('before 3rd yield')
    yield 3

gen = generator1()

value = next(gen)
print(value)

value = next(gen)
print(value)

value = next(gen)
print(value)

# value = next(gen) # gives a StopIteration error 
# print(sum(gen)) built in sum accepts generator
# print(sorted(gen)) built in sorted sorts the yielded values

def countdown(num):
    print('Starting')
    while num > 0: 
        yield num
        num -= 1

cd = countdown(4) # this invocation of countdown doesn't execute the countdown
value = next(cd)
print(value)

print(next(cd))

# advantage of generator
import sys

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num 
        num += 1 

print(sys.getsizeof(firstn(100000)))
print(sys.getsizeof(firstn_generator(1000000)))

# fibonacci
def fibonacci(limit):
    # 0, 1, 1, 2, 3, 5, 8, 13...
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
for i in fib:
    print(i)

# generator expressions
generator1 = (i for i in range(10000) if i % 2 == 0) # this is similar to list comprehension except that we use [] square brackets
print(sys.getsizeof(generator1)) # much more memory efficient

list1 = [i for i in range(10000) if i % 2 == 0]
print(sys.getsizeof(list1))
