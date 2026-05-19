# keywords - special reserved words that has a specific meaning
'''
if else while import except 
None is elif def class 
True break in for return try 
False continue
'''

# Identifiers - names that are given to variables, functions, classes and other objects
'''
Rules for naming identifiers :
1. Can only contain letters (A–Z or a–z), digits (0–9), and underscores (_). 
2. Must begin with a letter or an underscore. 
3. Can't use keywords as names. 
4. Python is case-sensitive: Sum and sum will be treated as two different identifiers. 
'''

# Variables - name that is given to a value so that it an be stored and later used in the program.
# container that where we keep datas (values)

# How python handles memory
'''
memory and garbage collection are done automatically
'''

# Basic I/O operations - 2 built in func tions - input and print
# number = int(input("Enter a number : ")) # type conversion
# print(number + 5)

# Data types :
'''
numeric - int, float, complex
string (str)
boolean (bool)
None type (None)
'''

# Type conversion also known as type casting
# implicit conversion - automatic conversion
# explicit conversion - manually converting

# Type checking
# print(type(10.5))
# print(isinstance(10, str))
a = 10
b = 10
print(id(a))
b = b + 10
print(id(b))
