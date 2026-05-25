# function - reusable block of code to do a particular task which can be called anywhere in the program

# Features
'''
Modularity
Reusability
Abstraction
Maintainability
'''

# three types of functions
'''
1. Built in functions - prebuilt functions in the programming language. eg: print(), input(), id(), isinstance()
2. User defined functions - defined by the user in the program
3. Lambda functions - anonymous functions
'''

# User defined function example
# Definition
def add_two_numbers(number_1, number_2 = 15):
    '''this is a function to add two numbers'''
    sum = number_1 + number_2
    return sum

# Calling
result = add_two_numbers(number_1 = 10)

# doctring - a string that is used to document what a function does
# help(print)

# Types of arguments
'''
1. Positional arguments - matched by position
2. Keyword argument - parameters are passed using names
3. Default arguments - assigned to parameters, so that even if no value is passed, the default is used
4. Variable length arguments - used when number of arguments is not available
eg : def print(*args)
5. Keyword varible length arguments - variable length arguments with a keyword
eg : def hi(**details)
hi(name="name", age="age", company="company")
'''

# Scope - an area in the program where a variable can be recognised and accessed

# local - declared inside a function. access only inside the function
# eg:
'''
def greet():
    message = "Hi" # local variable
    print(message)
'''

# global - declared outside every (any) function, which are accessible everywhere (inside and outside the function)
'''
message = "Hello" # global variable
def greet():
    print(message)
'''

# non-local (enclosing) - used inside nested functions (in the outer function)
'''def greet():
    message = "Hi"
    def hello():
        print(message)'''
        
'''def outer():
    x = "outer"
    
    def inner():
        # nonlocal x
        x = "inner"
        print(x)
        
    inner()
    print(x)

outer()'''

# Lambda - lambda functions are anonymous, single line, throwaway functions defined using the keyword 'lamdba'
'''
Syntax :
lambda arguments : expression
'''

'''s = lambda x,y : x * y
print(s(5, 6))'''

'''def square_of_a_number(x):
    return x * x

square = square_of_a_number(5)'''

# Recursion - a function calling itself
def factorial(n):
    if n == 0 or n == 1: # Base case
        return 1
    else: # Recursive case
        return n * factorial(n-1)

