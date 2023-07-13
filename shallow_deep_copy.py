# assignment operator
org = 5
cpy = org # creates a same variable to the same reference

cpy = 6
print(org)
print(cpy)

org_list = [ 0, 1, 2, 3, 4]
cpy_list = org_list
cpy_list[0] = -10
print(cpy_list)

# shallow v/s deep copy
# shallow is only one level deep and copies references of the nested objects
import copy
org_list1 = [0, 1, 2, 3, 4]
copy_list1 = copy.copy(org_list1)
# we can also make a shallow copy as below
copy_list2 = org_list1[:]

org_list2 = [[0, 1, 2, 3, 4], [5, 6]]
copy_list3 = copy.copy(org_list2)
copy_list3[0][1] = -10 # this modifies both the lists
print(copy_list3) 
print(org_list2)

# we need to make a deep copy to make the actual copy with copy.deepcopy()
# we can also use it for custom classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

p1 = Person('Alex', 55)
p2 = Person('Joe', 27)

company = Company(p1, p2)
company_clone = copy.copy(company)
company_clone.boss.age = 56
print(company_clone.boss.age) 
print(company.boss.age)

# we need to deep copy to only affect the copy
company_clone = copy.deepcopy(company) # makes a true copy
company_clone.boss.age = 57
print(company_clone.boss.age) 
print(company.boss.age)
