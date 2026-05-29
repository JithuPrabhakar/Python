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