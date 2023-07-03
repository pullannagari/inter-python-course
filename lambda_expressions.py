# small one line anonymous function
# lambda arguments: expression format
# evaluates the expression and returns the results
add10 = lambda x: x+10
print(add10(5))

# can have multiple params
mult = lambda x,y: x*y
print(mult(2,12))

# used in higher order functions, accepts functions as arguments
# sorted
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)

print(points2D)
print(points2D_sorted) # by default sorts with x

points2D_y_sorted = sorted(points2D, key=lambda x:x[1])
print(points2D_y_sorted)

# sorting according to the sum of each
points2D_sum_sorted = sorted(points2D, key=lambda x: x[0]+x[1])
print(points2D_sum_sorted)

list1 = [1, 2, 3, 4, 5]
list2 = map(lambda x: x*2, list1)
print(list(list2))

list3 = [ x*2 for x in list1 ]
print(list(list3))

list4 = [x for x in list1 if x%2 == 0]
print(list4)

from functools import reduce

# reduce 
list5 = reduce(lambda x, y: x*y, list1)
print(list5)

