# Functional programming is a methodology where programs are built using pure functions and immutable data
# pure functions - no side effects
# immutability - no changes (data is constant)

# First class function and Higher Order Function
# Python treats functions as first class objects that can be passed as arguments, returned and stored in variables
# First class functions - functions passed as an argument to another function (callbacks in js)
# higher order functions - functions that accepts another function as arguments (same name in js)
'''
def higher_order_function(first_clas_function_params):
    return first_clas_function_params()

def first_class_function_args():
    print("Hi")
    
higher_order_function(first_class_function_args)
'''

# Lambda functions
squares = lambda x : x * x
# in js -> squares = (x) => x * x

def squares(x):
    return x * x

# map(), filter(), reduce(), sort()
# map() - apply a function to all the items in an iterable
nums = [1, 2, 3, 4]
squared = list(map(lambda x : x * x, nums))
# squared = nums.map((x) => x * x) in js

# filter() - apply a condition to filter items in an iterable
evens = list(filter(lambda x : x % 2 == 0, nums))
# evens = nums.filter((x) => x % 2 == 0) in js

# reduce() - combine items in an itrerable into a single value
from functools import reduce
sum_of_items = reduce(lambda x, y: x + y, nums)
# sumOfItems = nums.reduce((x, y) => x + y, 0) in js

def sum_of_items(x, y):
    return x + y

# sort() - sorts items using a custom logic
names = ["Suresh", "Ramesh", "Ratheesh", "Anish"]
names.sort(key=lambda x : len(x))
# print(names)