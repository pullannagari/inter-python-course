# Strings: ordered, immutable, text representation

# we can use single or double quotes
string1 = "hello world \n"
string2 = 'welcome to strings'

print(string1 + string2)

# triple quotes are used for multiline strings
# used for documentation

string3 = """this
is 
a 
multiline
string"""
print(string3)

# another way to create multiline strings
string4 = "this \
    is \
        not a \
            multiline \
                string"
print(string4)

# indexing strings
print(string1[0]) # prints first character
print(string1[-1]) # prints the last character

# slicing
print(string1[6:])
print(string1[:5])
print(string1[::-1]) # reverse the string

# concatenation
greeting = "good evening"
name = "vivi"
concat_string = greeting + " " + name

print(concat_string)

# string iteration
for charc in concat_string:
    print(charc)

# check if a char or substirng inside the string 
if 'vi' in concat_string:
    print("yes")

# strings are immutable, cannot be changed
try:
    string4[5] = 's'
except TypeError as e:
    print(f"cannot change the string {e}")

# strip the remove the padded whitespaces, 
# doesn't change in place, creates a new string
padded_string = "     padding  "
print(padded_string.strip())

print(concat_string.upper()) # convert to upper case
print(concat_string.startswith("good"))

print(concat_string.find("oo")) # finds the index of the first occcurence
replaced_string = concat_string.replace("good", "very good")
print(replaced_string) # string replace

print(replaced_string.split()) # split string based on a delimeter, defaults to space
delimitted_string = "hello,this,should,be,delimtted"
splitted_strings = delimitted_string.split(',')
print(','.join(splitted_strings)) # joins each string in the list with the string

from timeit import default_timer as timer
str_list = ['a'] * 1000000

# print(str_list)

start = timer()
appended_list = ''.join(str_list)
# print(appended_list)
stop = timer()
print(stop - start)

# the above can be accomplished using a for loop, 
# but it is a very bad pythonic way of doing it.
# also the time taken for iterating is more compared to the pythonic way
start = timer()
iter_str = ''
for i in str_list:
    iter_str += i
#print(iter_str)
stop = timer()
print(stop - start)

# formatting strings
# f-strings, .format(), %
# using f-strings is recommended
float_var = 2.323232
print(f"we can also manipulate the value of the vars in f strings for ex. {float_var * 2}")





