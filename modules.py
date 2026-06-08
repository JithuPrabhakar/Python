# modules - a python file (.py) contains classes, functions or variables than can be reused in any other programs
# Advantages : Code reusability, Modularity, Maintainability.
# Any python file is a module

# Package : a directory (folder) containing a special __init__.py file along with one or more python modules.
# Sub packages : Package inside another package

# Types of Modules :
# 1. Built-in modules : already available in python installation. Eg: math, random, os, sys, datetime
# import math
# print(math.sqrt(49))

# 2. User-defined modules : created by users for custom functionalites
# Method 1: basic import
# import sample_module
# print(sample_module.greet("Akhil"))

# Method 2: importing specific function
# from sample_module import greet
# print(greet("Akhil"))

# Method 3: import with Alias
# import sample_module as sm
# print(sm.greet("Akhil"))

# 4. Method 4: import all
# from sample_module import *
# print(greet("Akhil"))

# 3. Third party modules : created by python community and installed using pip
# pip install third_party_module_name

# Naming convention
# lowercase, no special character, no uppercase, no spaces, no standard modules, consistent naming within a package

# Reloading a module :
'''
import importlib
import sample_module

importlib.reload(sample_module)
'''
