# OOP : is a programming paradigm that organizes code using Classes and Objects
# Features of OOP :
'''
Inheritance : Reusing the code from a parent class
Polymorphism : Same method different behaviours
Abstraction : Hiding implementation details
Encapsulation : Hiding internal data
'''

# Procedural programming : function based, Data and functions are separate, limited reusability
# programming languagaes that use Procedural : C, BASIC

# Object Oriented : Class and Object based, Data and functions are bundled, higher reusability
# programming languages that use OOP : Python, Java, C++, Javascript

# Benefits of OOP : reusability, maintainability, better code organization, scalability

# Class : Blueprint of an object
# Object : Instance of a class

# Defining a class
class Laptop:
    def __init__(self, brand, model): # constructor
        self.brand = brand # attributes
        self.model = model
        
    def browsing(self): # method
        pass
        
# Creating object
lenovo_i3 = Laptop("Lenovo", "i3")

# Self parameter : refers to the current instance (object), must be the first parameter in instance methods

# Attributes and Methods : attributes stores the state or data of an object.
# Methods are functions defined inside a class whoch defines the behaviour of an object

class Laptop:
    screen_size = 15.6 # class attribute. Class scope, accessible in all instances and class
    
    def __init__(self, brand, model, screen_size): # constructor
        self.brand = brand # instance attributes
        self.model = model # instance scope, accessible only via object
        self.screen_size = screen_size
        
    def browsing(self): # method
        default_browser = "Edge" # Local scope, accessible only in this method
        pass
    
# Shading (variable shadowing) : happens when an object variable has the same name as class variable, 
# which in turn hides the class variable

# Access Modifiers - control the visibility of class members
# public : members are accessible everywhere
# protected : members are accessible only within the class and its subclasses
# private : members are acccessible only inside the specified class

# public -
class Laptop:
    def __init__(self, name):
        self.name = name

# protected -
class  Laptop:
    def __init__(self, brand, name):
        self.brand = brand
        self._name = name # protected member
        
l1 = Laptop("Lenovo", "i3")

# print(l1._name)

# private - 
class Laptop:
    def __init__(self, brand, name):
        self.brand = brand
        self.__name = name
        
    def get_name(self):
        print(self.__name)
        
l2 = Laptop("Lenovo", "i5")

# l2.get_name()

# print(l2.__name)

# Name mangling - python changes the name of the private variable to _Classname__member internally
# print(l2._Laptop__name)

# Inheritance - allows one class to acquire the attributes and methods of another class
# the class that acquires the members - Child/Derived class
# the class from which the members are acquired - Parent/Base class

class Person:
    def __init__(self, name):
        self.name = name
        
    def hi(self):
        print(f"{self.name} says hi")
        
class Student(Person):
    def hi(self):
        super().hi() # Super function - used to call methods or constructors of the parent class from a child class
        # print(f"{self.name} says Hello")
        
    def study(self):
        print(f"{self.name} is studying")
        
s1 = Student("Anil")
s2 = Student("Ram")
p1 = Person("Hari")
# p1.study()

# s1.hi()

# Types of Inheritance - 5 types in python
# Single inheritance - one child -> one parent
class Iphone():
    pass

class Iphone_17(Iphone):
    pass

# Multilevel inheritance - child inherits from parent which inturn inherits from another parent
class Iphone:
    pass
class Iphone_17(Iphone):
    pass
class Iphone_17_pro(Iphone_17):
    pass

# Multiple Inheritance - child ineherits from more than one parent
class Iphone:
    def hi(self):
        print("iphone")
        
class Ipad:
    def hello(self):
        print("Ipad")
        
class Iphone_17_pro_max(Ipad, Iphone):
    pass

i17 = Iphone_17_pro_max()

# i17.hi()
# i17.hello()

# MRO - Method Resolution Order (using C3 linearization algorithm) - used whenmultiple inheritance is involved

# Hierarchical inheritance - one parent and multiple children
class Iphone:
    pass
class Iphone_16(Iphone):
    pass
class Iphone_17(Iphone):
    pass

# Hybrid Inheritance - combination of two or more types of inheritance
class Iphone:
    pass
class Iphone_16(Iphone):
    pass
class Iphone_17(Iphone):
    pass
class Iphone_17_pro_max(Iphone_17):
    pass


# Polymorphism - allows same method, function or operator to behave differently based on context or object type - enhances code flexibility and reusabillity

# Funciton/Method - a single function or method behaves differently based on the number or data type of the arguments
# print('123.25', 123)

# user defined function polymorphism
class Student:
    def show_details(self, name=None): # different number of arguments
        if name:
            print("Student name provided")
        else:
            print("No name provided")
    
s1 = Student()
# s1.show_details()

class Calculator:
    def add(a, b): # different types of arguments
        if isinstance(a, int) and isinstance(b, int):
            return int(a) + int (b)
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        else:
            return f"a and b are not supported data types"
        
c = Calculator()
# c.add(1, 2)
# c.add('1', '2')

# Operator overloading - lets define custom behaviour for python operators
class Student:
    def __init__(self, marks):
        self.marks = marks
        
    def __add__(self, other):
        return self.marks - other.marks
    
s1 = Student(80)
s2 = Student(85)
# print(s1 + s2)

# Duck Typing - type or class of an object is less important than the methods it defines
class Student:
    def code(self):
        print("Student is coding")
        
class Teacher:
    def code(self):
        print("Teacher is coding")
        
def start_coding(person):
    person.code()
    
s = Student()
t = Teacher()

# start_coding(s)
# start_coding(t)

# Method overloading - multiple methods with same name but different parameters, this is not supported by python natively 
# but can be mimicked using default arguments
class Student:
    def show_details(name=None, *args):
        pass

# Method Overriding - allows a method in Child class to redefine the method in Parent class
class Person:
    def show():
        pass
class Student(Person):
    def show():
        pass
    
# s = Student()


# Encapsulation - wrapping of methods and attributes to a single unit (class) and restricting direct access
class Student:
    def __init__(self):
        self.__name = ""
    
    def set_name(self, name): # setter
        if name.isalpha():
            self.__name = name
        else:
            print("Invalid format")
            
    def get_name(self): # getter
        return self.__name
    
# Abstraction - hiding implementation details and showing only the essential features
from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def work(self):
        pass
    
class Student(Person):
    def work(self):
        print("student is studying")
        

# Constructor - __init__() - magic (special) method in python which is automatically called when creating a new object.
# It is used to initialize object attributes
class Sample:
    def __init__(self, name): # Constructor
        self.name = name # initialization

s1 = Sample("demo")

# Destructor - __del__() - automatically called when an object is about to be destructed
class Sample:
    def __init__(self, name): # Constructor
        self.name = name # initialization
        
    def __del__(self):
        print(f"{self.name} is deleted")

s1 = Sample("demo")
del s1

# Object lifecycle - stages of an object
# 1. Objet creation - __init__()
# 2. Object usage - accessing attribues, calling methods
# 3. Object destruction - __del__()

# Class method and static method
class Laptop:
    screen_size = 15.6 # Class attribute
    def __init__(self, name):
        self.name = name # instance attribute
        
    def hello(self): # instance method
        pass
    
    @classmethod
    def hi(cls):
        print(f"Hi, laptop kittiyo? cls.screen_size()")
    
    @staticmethod
    def hi():
        pass