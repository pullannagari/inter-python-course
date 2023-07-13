# different use cases of * sign in python

# multiplication
result = 5 * 7
print(result)

result = 2 ** 4 # power operation
print(result)

zeros = [0]*10 # creates a list with 10 elements, with each element as 0
# we can also have some initial values for the list
list1 = [0, 1, 2, 3]*3 # repeats 0, 1, 2, 3 three times
print(list1)

tuple1 = (0, 1)*3
print(tuple1) # repeats 0, 1 tuple three times

string1 = "AB" * 10
print(string1)

# variable arguments
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args: # args is a tuple
        print(arg)
    for key in kwargs: # kwargs is a dict
        print(key, kwargs[key]) 

foo(1, 2, 3, 4, 5, six=6, seven=7)

def foo1(a, b, *, c):
    print(a, b, c)

foo(1, 2, 3, 4, c=5)

list2 = [0, 1, 2]
foo(*list2) # can use list as the argument but need to match the length of the list

# can also use dict, but the keys need to match with the parameter names but also need ** two stars

# for unpacking containers
numbers = [ 1, 2, 3, 4, 5, 6]
*beginging, last = numbers
print(beginging)
print(last) # we can also unpack from the beginging side or middle
beginging, *middle, last = numbers
print(middle)

# can be used to merge tuple and a list
tuple1 = (1, 2, 3)
list2 = [4, 5, 6]

new_list = [*tuple1, *list2] # also works with sets
print(new_list)

dicta = { 'a': 1, 'b': 2}
dictb = { 'c': 3, 'd': 4}
new_dict = {**dicta, **dictb}
print(new_dict)
