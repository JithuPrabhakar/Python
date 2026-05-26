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