"""
- The difference between arguments and parameters
    parameters are variables defined or used inside parantheis while defining a function, while arguments are the values passed when calling the function
- Positional and keyword arguments
    we can pass arguments as positional or keyword arguments
    foo(1, 2, 3) or foo(c=3, b=2, a=1) is same
    we cannot use positional argument after keyword argument
    foo(1, b=2, c=3) this works
    foo(1, b=3, 3) this wouldn't work
    foo(1, b=2, a=3) this wouldn't work as well
    using keyword arguments imporves readablity
- Default arguments
    default arguments should be defined at the end of the funtion definition
    def foo(a, b, c, d=4) 
    you can then invoke the func as 
    foo(1, 2, 3) or foo(1, 2, 3, 5)
- Variable-length arguments (*args and **kwargs)
    def foo(a, b, *args, **kwargs)
    if we mark a function parameter with single *, then we can pass multiple number of postional args
    if we mark a function parameter with double *, then we can pass multiple keyword arguments
    we can enfore keyword only args
- Container unpacking into function arguments
- Local vs. global arguments
- Parameter passing (by value or by reference)
"""

def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])

foo(1, 2, 3, 4, 5, six=6, seven=7)
foo(1, 2, six=6, seven=7)
foo(1, 2, 3, 4)

# unpacking the list
def foo1(a, b, c):
    print(a, b, c)

list1 = [0, 1, 2]
foo1(*list1) # we need to make sure the length of the list matches the number of parameters

# unpacking the dict
def foo2(a, b, c):
    print(a, b, c)


dict1 = {'a': 1, 'b': 2, 'c': 3}
foo2(**dict1) # note we are using 2 *'s and also the keys must match the param names

# local v/s global variables

def foo3():
    global number
    x = number
    number = 3 # raises an error since, it will try to create a local variable with the same name, we use global to refer to the global variable
    print('number inside foo3:', x)

number = 0
foo3()
print('number in the main:',number)

# call by value v/s call by refernce
# python is call by python object reference
# the parameter passed in is a refernce to the object, but the reference is pass by value
# mutalble objects like lists, dicts can be changed in a method. if we rebind the refernce then the outer reference stll continues with the old list
# immutable objects like strings cannot changed within a method, but immutable objects within a mutable object can be rebinded
