# Scientific form Numbers
_sci_form = 1.23E-7  # 0.000000123 = 1.23 x 10^7
_another_sci_form = 1.23E-7
print(type(_sci_form))  # will display <class 'float'>
print(_sci_form-_another_sci_form)  # 0.0

'''
We can define numbers in scientific form. Scientific form = a x 10^b . In Python we can define sci-form as
aE-b
'''

# Complex Numbers

'''
We can define complex numbers as realNumber+ImaginaryNumber(J)
Example: In Math we write 3+2i, in python 3+2j
'''
_complex_number = 3+2j
print(_complex_number)  # (3+2j)
print(type(_complex_number))    # <class 'complex'>

# not Operator
print(not (200 == 210))  # True
print(not ("Java" == "Java"))  # False

# or Operator

print((100 < 200) or (55 < 6))  # True
print((100 < 99) or (55 < 6))  # True.
'''
In above case, (100>99) is True, and so is the whole logical expression. 
Hence there is no need to evaluate the expression (55<6).
'''
# Truthy and Falsy values

'''
 Truthy Values : Values which are equivalent to 'True' is known as Truthy values.
 Falsy Values: Values which are equivalent to 'False' is known as False values.
 
 Falsy Values in Python:
 None, False, 0, 0.0
 Empty Sequence (List) for example, '', [], ()
 Empty Dictionary for example, {}
 
 We can check whether the value is Truthy or Falsy using bool(value_to_find) 
 
'''
print(bool(0))  # False
print(bool(''))  # False
print(bool([]))  # False
print(bool({}))  # False

# bool type

'''
A bool type represents only two state  true or false. In Python we define bool types using reserved keyword 'True' and 
'False'
Python uses 1 and 0 to represent true and false.We can verify this fact by using int() function on True and False 
keywords. 
'''

print(int(True))  # 1
print(int(False))  # 0

# Breaking single statements into multiple lines
'''
Python allows us to break long expression into multiple lines using line continuation symbol ( \ ). 
The \ symbol tells the Python interpreter that the statement is continued on the next line. 
For example:
'''

_long_variable = "Hello Hello Hello Hello Hello Hello Hello Hello Hello" \
                 " Hello Hello Hello Hello Hello" \
                 " Hello Hello Hello Hello Hello Hello Hello Hello "
print(_long_variable)

# Type conversion
'''
int(), float(),str() function can be used for type conversion
'''
print(int("2"))  # 2











