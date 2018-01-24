# type is used to find  type of the variable.
int_type = type(1)
print(int_type)
str_type = type("Java")
print(str_type)

# Variable Declaration
language = "Python"
version = 2.7

'''
We can't define variable type like cpp and java, If we do python interpreter will give an error.
Example : str oop_language = "Java"
'''

'''
Python automatically detects the type of the variable and operations that can be performed on it based on the type
of the value it contains. In programming jargon this behavior is known as Dynamic Typing. It means that we could use
the same variable to refer to a data of completely different type than it initially points to.
Example:
'''
android_latest_version = 8.1
print(android_latest_version)
print(type(android_latest_version))

android_latest_version = "Eight point one"
print(android_latest_version)
print(type(android_latest_version))

'''
When we assign new value to a variable the reference to old value is lost. For example, when "Eight point one" is 
assigned to the android_latest_version, the reference to value 8.1 is lost. At this point, no variable is pointing 
to that memory location. When this happens Python Interpreter automatically removes the value from the memory 
through a process known as garbage collection.
'''

'''
If you try to access a variable before assigning any value to it. You will get NameError error like this:
age
print(age)
will get NameError: name 'age' is not defined
'''
'''
Python is case-sensitive language which means that HOME and home are two different variables
'''
BUG_TICKET = 1
bug_ticket = "001"

# Multiple items printing
lan = "Python" # lan can be any data type
print("Java", lan, "Php")

# Simultaneous Assignment
oracle, google, apple, microsoft = "Java", "Android", "Swift and IOS", ".NET"
print(oracle)

# Swapping values
'''
In other programming languages to swap we need third variable
Example: 
    int i = 10, j = 20;
    int tmp;  // variable to store data temporary 
    tmp = i;  // now tmp contains 10
    i = j;  // now i contains 20
    j = tmp;  // now j contains 10
    
'''
i, j = 10, 20
print(i, j)

i, j = j, i
print(i, j)

# Functions
'''
 If a function do not explicitly return any value then it returns a special value called None, which is one of 
 reserved keywords in Python.
'''

# Modules
'''
Python uses modules to group similar function, classes, variables etc. For example, math module contains various 
Mathematical functions and constants, datetime module contains various classes and functions for working with 
date and time and so on. To use functions, constants or classes defined inside the module, we first have to import it 
using the import statement. The syntax of the import statement is as follows:

import module_name

To use a method or constant from the module type module name followed by the dot (.) operator.
'''

import math
print(math.pi)

'''
Built-in functions like print(), type(), input() belongs to 
a special module called __builtin__. But Why it is special ? Because functions inside the __builtin__ module are 
always available to use without explicitly importing __builtin__ module.

'''

# Reading Input from Keyboard

_user_input = input("Please Enter your name: ")
print("User's name is:", _user_input)
