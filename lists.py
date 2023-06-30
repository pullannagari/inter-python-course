# lists: ordered, mutable, allows duplicate elements
list1 = ["banana", "apple", "cherry"]
print(list1)

# list allows for different types to be stored
list2 = ["multitype", 1, True]
print(list2)

item = list2[-1]
print(item) # prints True since it refers to the last element

for element in list1:
    print(element) # prints individual elements

if "banana" in list1: # check if an element is present in a list
    print("found banana") 

print(len(list1)) # to check the number of elements inside a list

list2.append(1233.23)
print(list2) # appends to the end of the list

list2.insert(2, "insertedatPosition")
print(list2)

list2.pop() # returns the last element and removes from the list
print(list2)

list2.append("multitype")

list2.remove("multitype") # removes the first occurence of \
                          # specific element left to right
print(list2)
list2.remove("multitype") # removes the second occurence
print(list2)

#list1.remove("multitype") # results in value error

list2.clear() # removes all the elements
print(list2)

list1.reverse() # reverses the list in place
print(list1)

list2 = sorted(list1) # create a copy of the sorted list
print(list2)

list1.sort() # sorts the list in place (Merge sort)
print(list1)

list3 = [0]*10
print(list3)

list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list5 = [10, 11, 12, 13, 14, 15]

print(list4+list5)

# slicing the list
print(list4[:5])
print(list4[1:5])
print(list4[5:])
print(list4[::2])
print(list4[::-1])

# copying the list
list6 = list5.copy()
print(list6)

# other ways of copying the list
list7 = list(list6)
print(list7)

# list comprehension
squared_list = [ i * i for i in list4] # syntax is expression followed by loop

print(squared_list)




