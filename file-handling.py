'''File handling allows a Python program to store data permanently in files on disk, read 
it later, and exchange data with external files. It supports reading and writing both text and binary files.'''

# open() function
# file_object = open("filename.extension", "mode")
'''
Modes
'r' - read (default)
'w' - write
'a' - append
'x' - Create (new file only)
'b' - binary
't' - text mode
'+' - read and write
'''
# close() function
'''
f = open("data.txt", 'r')
# perform any file operations
f.close()
'''

'''
f = open('data.txt', 'r')
f.name # file name
f.mode # access mode
f.closed # return true if the file is closed else false
f.close() # closes the file
'''

# f = open('data.txt', 'a')
# print(f.read()) - read the entire document
# print(f.readline()) - reading the first line followed by the other lines one by one
# print(f.readlines()) - returns a list containing all the individual lines
# f.write("This is a new line writing") - deletes old data and replace with new parameter
# f.writelines(["This is a new line writing\n", "Second line\n"]) - writes multiple lines
# f.write("This is appended") - use the mode 'a' for appending
# f.close()

# with statement - automatically closes file
# f = open('data.txt', 'w+')
'''with open("data.txt", 'w+') as f:
    f.write("This is a new file")
    print(f.tell())
    f.seek(0)
    print(f.read())'''
# f.close()
    
# Exception handling
'''try:
    f = open("data.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File Not Found")
finally:
    f.close()'''
    
# Serialization : process of converting python objects into another format (pkl or json)
# pickle module : used to serialize and deserialize python objects to binary format
# dump() - serialize - converts python object ot binary
# load() - deserialize - converts binary to python object
'''import pickle
data = { "name": "Some name", "age": 20 }
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)
    
with open("data.pkl", "rb") as f:
    data = pickle.load()
    print(data)'''

# json module : used to serialize and deserialize python objects to json format (language-independant and human readable)
# dump() - serialize - converts python object ot binary
# load() - deserialize - converts binary to python object
'''import json
data = { "name": "Some name", "age": 20 }
with open('data.pkl', 'w') as f:
    json.dump(data, f)
    
with open("data.pkl", "r") as f:
    data = json.load()
    print(data)'''
