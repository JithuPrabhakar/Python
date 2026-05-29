# data structure - is a way to organize and store data so that it can be used efficiently
# sequence - ordered collection of elements (characters, numbers etc)

# Strings - sequence of characters
string_1 = 'strings inside single quotes'
string_2 = "strings inside double quotes"

multi_line_string = '''this is a 
multi line
string'''

string_in_string = 'there are seven "wonders" in the world'
# print(string_in_string)

string = "Hello World"
# print(string[4])
# print(string[::-1])

# string = "HellocWorld"
# print(string)

# string = string + " Hi"
# string += " Hi"
# print(string)

# Escape characters
# print("Hi H\\ello")

# format() method
ending = ","
string = "Hello{} World".format(ending)
# print(string)

# f-string
name = "Abhijith"
age = 30
# print(f"{name} is {age} years old")

# Common string methods:
'''
upper()
capitalize()
replace()
find()
split()
join()
'''

# len function - to determine the number of elements in a sequence
# print(len(string))


# List - is a collection of ordered, mutable elements that can hold multiple elements in a single variable
ls = [1, 2, 3, 4, 5]
# print(ls[1:4])
ls[3] = 6
# print(ls)

# List methods :
'''
append()
insert()
remove()
pop()
sort()
reverse()
clear()
'''

# sorted(ls)

nested_list = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]

a = [5]
b = [5]
# print(a == b)

# Tuples - ordered, immutable collection of elements
tp = (1, 2, 3, 4, 5)
tp = list(tp)
tp = tuple(tp)

# tuple unpacking - assigning the elements of a tuple to individual variables in a single line
tp = (1, 2, 3, 4)
var_1, var_2, var_3, var_4 = tp
'''
var_1 = 1
var_2 = 2
var_3 = 3
var_4 = 4
'''


# Sets - unordered, unidexed collection of elements which does not allow duplicate elements (elements will be unique). Set is mutable but elements must be immutable
set_1 = {1, 2, 4, 2}
set_2 = set([1, 2, 3])

# for element in set_1:
#     print(element)
    
set_1.discard(2)

# print(set_1)

# Set operations
# Union - returns all the unique elements from both sets (| or union())
a = {1, 2, 3}
b = {3, 4, 5}
# print(a.union(b))
# Intersection - returns all the common elements of both the sets (& or intersection())
# print(a&b)
# Difference - returns elements from the first set, which ae not in the second (- or difference)
# print(a - b)
# Symmetric Difference - returns all the elements in either set, but not both (^ or symmteric_difference)
# print(a^b)

# Frozenset - same as set but immutable
fs = frozenset([1, 2, 3])

sentence = "I am Sooraj and I am a computer science engineer"

# find the unique elements from a list without using set
list_1 = [1, 2, 3, 4, 5, 1, 3, 4]
list_2 = []
for current_element in list_1:
    if current_element not in list_2:
        list_2.append(current_element)
        
# List comprehension
number_list = [1, 2, 3, 4, 5]
squares = []
for x in number_list:
    squares.append(x * x)
    
squares = [x*x for x in number_list]

# Mapping in Python - collection of key-value pairs
# the built-in mapping type in python - dictionary (dict)

# Dictionary : collection of key-value pairs and each key will be unique and each key will map to a value
sample_dictionary = { "key_1": "value_1"}
sample_dict = dict(city="Trivandrum", state="Kerala")

# accessing dictionary elements
# print(sample_dict["city"])

# add and update to dictionary
sample_dict["country"] = "India" # add
sample_dict["city"] = "Kazhakkoottam" # update
# print(sample_dict["country"])

# Removing
# del sample_dictionary["key_1"]
# sample_dictionary.pop("key_1")
# print(sample_dictionary)

# Looping through dictionaries
# for keys in sample_dict:
    # print(keys, sample_dict[keys])
    
# for keys in sample_dict.keys():
    # print(keys, sample_dict[keys])
    
# for keys, values in sample_dict.items():
#     print(keys, values)
    
# for values in sample_dict.values():
#     print(values)

# Nested dictionary - dictionary inside dictionary
employee = {
    "emp_1" : { "name" : "Jithu", 'age': 35 },
    "emp_2" : { "name" : "Thara", 'age': 35 }
}

# print(employee["emp_1"][name])

# Dictionary Method
'''
get()
keys()
values()
items()
update()
pop()
clear()
copy()
'''

# Dictionary keys must be immutable and unique and stored efficiently using Hashing
# Hashing : the process of converting data into a fixed size integer called Hash value or Hash code.
# Python uses hashing for Sets and Dicitonaries

# None : a special built-in constant in python which represents the absence of a value