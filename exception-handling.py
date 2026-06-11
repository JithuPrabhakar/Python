# Exceptions - are runtime errors that disrupt the normal fl;ow of the program
# Syntax Error vs Exceptions
# syntax - came form code and can be detected before running
# exceptions - can only be detected at the runtime

# Common Exceptions:
# 1. ZeroDivisionError - divide by zero
'''Exception
marks = 90
subjects = 0
average = marks/subjects'''

'''Exception Handling
try:
    marks = 90
    subjects = 0
    average = marks/subjects
except ZeroDivisionError:
    print("You cannot divide by zero")'''
    
# 2. TypeError - object with inappropriate
# 3. NameError - variable is not defined
# 4. IndexError - index out of range of a list or a tuple
# 5. ValueError - correct data type but inappropriate value
'''try:
    user_input = 'twenty'
    if int(user_input) > 18:
        pass
except ValueError:
    print("Please use correct value")'''
# 6. KeyError - key not found in dictionary
# 7. AttributeError - invalid attribute is accessed for an object
# 8. ImportError/ModuleNotFoundError - imported module cannot be found
# 9. IndentationError/SyntaxError - not written proper syntax (indentation)

# Multiple Exception -
'''try:
    x = int("A")
    y = 10/0
except (ValueError, ZeroDivisionError) as e:
    print("Error", e)
else:
    pass
finally:
    pass'''
    
# else with try - runs when no exception occurs
# finally - exception or not, the block should run

# Manual Exceptions
# syntax : raise ExceptionType("Custom Error Message")
'''age = -1
if age < 0:
    raise ValueError("age should be greater than 0")'''

# Custom Exception -
class NegativeNumberError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise NegativeNumberError("age should be greater than 0")

# check_age(-1)