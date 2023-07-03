# a python program terminates as soon as there is syntax error or an exception

# syntax errors: syntactically incorrect statement
# ex. incorrect number of closing braces print(()

# a = 5 + '10' # raises TypeError

# common type of exceptions
# ModuleNotFoundError
# import somemodule # raises ModuleNotFoundError

a = 5
# NameError
# b = c # raises NameError: name not defined

# FileNotFoundError
# f = open('somefile.txt')

# ValueError
# raised if incorrect/unknown value is passed
a = [1, 2, 3]
# a.remove(4) # raises ValueError

# a[3] raises IndexError

dict1 = {"name":"vivi"}
# dict1["age"] raises KeyError

# x = -5
# if x < 0:
#     raise Exception("x should be postitive") # custom errors

x = -4 
# assert(x>=0), 'x is not postitive'
# gives a AssertionError since x is negative

try:
    a = 5 / 0
except ZeroDivisionError as zde:
    print(zde)

try:
    a = 5 / 1
    b = a + '10'
except ZeroDivisionError as zde:
    print(zde)
except TypeError as te:
    print(te)
else: # runs if there's no exception
    print('code executed fine')
finally: # runs always, meant for clean up operations
    print('in finally')


# we can custom error classes
class ValueTooHighError(Exception):
    pass

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')

try:
    test_value(200)
except ValueTooHighError as vthe:
    print(vthe)

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_small_value(x):
    if x < 10:
        raise ValueTooSmallError("value is less than 10", x)

try:
    test_small_value(1)
except ValueTooSmallError as vtse:
    print(vtse)