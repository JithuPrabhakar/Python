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
from functools import reduce # functools contains necessary tools for functional programming
sum_of_items = reduce(lambda x, y: x + y, nums)
# sumOfItems = nums.reduce((x, y) => x + y, 0) in js

def sum_of_items(x, y):
    return x + y

# sort() - sorts items using a custom logic
names = ["Suresh", "Ramesh", "Ratheesh", "Anish"]
names.sort(key=lambda x : len(x))
# print(names)

# Lambda constructor in Python - refers to a lambda function inside a constructor
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.status = (lambda m : "Pass" if m >= 40 else "Fail")(marks)
        
s1 = Student("Akhil", 30)
# print(s1.status)

# Comprehensions
# list comprehension - squares = [x*x for x in range(5)]
# set comprehension - unique = {x for x in [1, 2, 2, 3]}
# dict comprehension - square_dict = {x : x * x for x in range(5)}

string = "String"
list_of_char = [char for char in string]
# print(list_of_char)

numbers = [1, 3, 5, 7, 9]
num_dict = {x : x**3 for x in numbers}

sentence = "the quick brown fox jumps over the lazy dog"

even_odd = [x if x%2==0 else "Odd" for x in range(1, 11)]

numbers = [[1, 3, 5], [7, 9, 2], [3, 5, 7], [9, 1, 2]]

# Iterables and Iterators : Iterable is a collection and Iterator is the object that refers to the current item in the collection

# fruits = ['apple', 'orange', 'grape', 'pineapple', 'mango']

# for fruit in fruits:
#     print(fruit)

# it = iter(fruits)

# while True:
#     try:
#         item = next(it)
#         print(item)
#     except StopIteration:
#         

# print(next(it))
# print(next(it))
# print("next item")
# print(next(it))

# Generator
def counter():
    n = 1
    while True:
        yield n
        n += 1
    
count = counter()
# print(next(count))
# print(next(count))

# __iter__() and __next__()

class Count: 
    def __init__(self, min, max): 
        self.max = max
        self.min = min
        # self.step = step
        if min == 0:
            self.current = -1
        if min > 0:
            self.current = min-1
    def __iter__(self): 
        return self
    def __next__(self):
        if self.current < self.max-1:
            self.current += 1
            return self.current
        raise StopIteration
    
# for num in Count(2,6):
#     print(num)