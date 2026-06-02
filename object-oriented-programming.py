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