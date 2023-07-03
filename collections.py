# collections: Counter, namedTuple, OrderedDict, defaultDict, deque

# Counter
from collections import Counter

stra = "aaaaabbbbcccc"
char_counter = Counter(stra)
print(char_counter)

lista = ["lajd", "jslja", "aljd", "lajd", 1, 1, True, False]
char_counter = Counter(lista) # can be used with different iterables
print(char_counter)
print(char_counter.most_common(1)) # most common item with the count as a tuple
print(char_counter.most_common(2)) # top 2 most common elements with their counts

print(char_counter.most_common(1)[0][0]) # top element
iter_ele = char_counter.elements() # returns iterable elements
print(list(iter_ele))

# namedtuple
# easy to create light weight object type, similar to struct
from collections import namedtuple
Point = namedtuple('Point', 'x,y') # creates a class with x and y properties
point1 = Point(1, 2)
print(point1)
print(f"x: {point1.x}")


# OrderedDict
from collections import OrderedDict
# similar to dict, but remembers the order of insertion
# became less relavant now since the built in dict already comes with this feature
ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["z"] = 26
print(ordered_dict)
print(ordered_dict.get("z"))


# defaultdict
from collections import defaultdict
# similar to dict, but gives a default value if the key has not been set yet
dict1 = defaultdict(int) # give a default type
dict1['a'] = 1
dict1['b'] = 2
print(dict1['a'])
print(dict1['c']) # prints 0 as the default int value, instead of the error

# deque
# a double ended queue
# used to add/removes the elements from both the ends
# implemented to be efficient
from collections import deque
deque1 = deque()

deque1.append(1)
deque1.append(2)
deque1.appendleft(3)
print(deque1)
deque1.pop()
print(deque1)
deque1.popleft()
print(deque1)
deque1.extend([2,3,4])
print(deque1)
deque1.extendleft([7,8,9])
print(deque1)

deque1.rotate(1) # rotate one place to the right
print(deque1)
deque1.rotate(-1)
print(deque1)