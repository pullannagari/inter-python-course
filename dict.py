# Dictionary: unordered, mutable, key-value pairs

dict1 = {"name": "Sud", "age": 34, "city": "Portland"}
print(dict1)

#another way of creating a dict
dict2 = dict(name="Shar", age=32, city="Phoenix")
print(dict2)

print(dict1["name"])

# print(dict2["phone"]) # results in KeyError

#dictionary is mutable
dict1["phone"] = 123434532323
print(dict1)

#deleting a Key:Value pair
del dict1["phone"]
print(dict1)

print(dict1.pop("age")) # pops from the dict and returns its value
print(dict1)

print(dict1.popitem()) # removes the last inserted item and returns the key value pair as tuple

if "lastname" in dict1:
    print("lastname in dict")

try:
    print(dict1["lastname"])
except KeyError as ke:
    print(f"inside except: {ke} not found")


for key in dict2: # loops through all the keys
    print(key)


for key in dict2.keys(): # another way to loop through the keys
    print(key)


for val in dict2.values(): # iterate through the values
    print(val)


for key, val in dict2.items():
    print(f"key: {key}, val: {val}") # prints key and value


# copying a dictionary

# most common way is using 
dict3 = dict2.copy()
print(dict3)

# another way to copy 
dict4 = dict(dict2)
print(dict4)

print(dict1)
# merging two dictionaries will overwrite the values from another dict and add the non-existent keys
dict1.update(dict2)
print(dict1)

# possible key types are any immutable types like numbers, tuples
dict5 = {3: 9, 6:36, 9: 81}
print(dict5[3])

# another alternative
dict6 = { (1, "hey"): "this is one", (2, "hello"): "this is two"}
print(dict6)
print(dict6[(1, "hey")])
try:
    print(dict6[(1,)]) # throws KeyError exception since (1,) tuple is not found
except KeyError as e:
    print(f"exception occurred {e}")

