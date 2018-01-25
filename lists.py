# Sequences

numbers = [1, 2, 3, 4, 5]
print(numbers)

'''
A sequence is term used to refer  data types which hold multiple items. Python have several types of sequences. 
Following are most important.
1. list
2. tuples
3. string
'''

# list
'''
A list is sequence of items separated by comma (,) with in the square brackets ([])
example:
_my_variable = [item1, item2,.......itemN]
NOTE : A list is an object and is of type 'list'
The '_my_variable' variable do not store the contents of the list, it only stores a reference to the address where list 
object is actually stored in the memory.
'''
_languages = ["Java", "Php", "Python"]
print(type(_languages))  # <class 'list'>

'''
A list can contain same or different type of elements
'''
_languages_versions = ["Java", 9, "Python", 3.7]
print(_languages_versions)  # ['Java', 9, 'Python', 3.7]


'''
Creating empty list
'''
_empty_list_way_1 = []
print(_empty_list_way_1)  # []

_empty_list_way_1.append(1)
print(_empty_list_way_1)  # [1]

'''
Creating empty list
'''
_empty_list_way_2 = list()
print(_empty_list_way_2)  # []

_empty_list_way_2.append(2)
print(_empty_list_way_2)  # [2]

'''
Creating list with elements by creating list object
'''
_list_obj_1 = list(["Java", 9, "Python", 3.7])
print(_list_obj_1)  # ['Java', 9, 'Python', 3.7]

_list_obj_2 = list("Java")
print(_list_obj_2)  # ['J', 'a', 'v', 'a']

'''
list with nested list
'''
_inner_list_1 = [1, 2, 3, 4]
_inner_list_2 = ["Java", "Php", "Python"]
_outer_list = [_inner_list_1, _inner_list_2]
print(_outer_list)  # [[1, 2, 3, 4], ['Java', 'Php', 'Python']]

'''
list with nested list
'''
_outer_list_object_1 = list([_inner_list_1, _inner_list_2])
print(_outer_list_object_1)  # [[1, 2, 3, 4], ['Java', 'Php', 'Python']]

_outer_list_object_2 = list()
_outer_list_object_2.append(_inner_list_1)
_outer_list_object_2.append(_inner_list_2)
print(_outer_list_object_2)  # [[1, 2, 3, 4], ['Java', 'Php', 'Python']]

'''
creating list using range()
'''

_range_list = list(range(5))
print(_range_list)  # [0, 1, 2, 3, 4]

_range_list = list(range(2,4))
print(_range_list)  # [2, 3]

_range_list = list(range(2, 8, 2))
print(_range_list)  # [2, 4, 6]

'''
using builtin functions with list
'''
print(len(_range_list))  # 3

print(max(_range_list))  # 6

print(sum(_range_list))  # 12

'''
Accessing list elements using index
'''
print(_range_list[0])  # 2

'''
We can access a list using -ve index. -ve means accessing elements in reverse order

'''
# -1 == last element
# -2 == last-1 element
# -3 == last -2 element
print(_range_list[-1])  # 6

'''
lists are mutable, which means we can add/delete/edit elements form it.
'''

_mutable_list = ["Java", "Python"];
print(id(_mutable_list))  # id is used to find memory address ; 139644521638600

_mutable_list.append("Php")
print(id(_mutable_list))  # id is used to find memory address ; 139644521638600

'''
Iterating list elements using for loop
'''
_iteratble_list = [1, 2, 3, 4, 5]
# We can change the value of the variable 'element' without effecting _iteratble_list, i.e., change to 'element' doesn't
# change the _iteratble_list contents
for element in _iteratble_list:
    print(element)  # prints each element in the _iteratble_list

'''
Membership operator in and not in operator
'''
_currency = ["$", "rs", "p"]
if "d" not in _currency :
    print("invalid currency")
else:
    print("Valid currency")

if "$" in _currency :
    print("Valid currency")
else:
    print("invalid currency")

'''
list concatenation
'''
_books = ["Effective Java", "Java Concurrency in Practice ", "Filthy Rich Clients"]
_authors = list(["Josh Bloch", "Brain", "Guy and Chet"])

_books_authors = _books+_authors
print(_books_authors)  # ['Effective Java', 'Java Concurrency in Practice ', 'Filthy Rich Clients', 'Josh Bloch', 'Brain', 'Guy and Chet']

# Repetition operator

_list_scores = [200, 201, 340, 399]
_list_scores_4x = _list_scores * 4
print(_list_scores_4x)  # [200, 201, 340, 399, 200, 201, 340, 399, 200, 201, 340, 399, 200, 201, 340, 399]

'''
using compound operator (compound operators for list are *=, +=)
By using compound operator we can re-assign new value to the old variable instead of creating new variable as above.
'''

_list_scores *= 2
print(_list_scores)  # [200, 201, 340, 399, 200, 201, 340, 399]

_list_scores += [1, 2]  # [200, 201, 340, 399, 200, 201, 340, 399, 1, 2]
print(_list_scores)

# Comparing lists

'''
We can compare lists using relational operators (>, <, >=, <=, != , ==). list comparision works when the two lists have
same type of elements.The process starts off by comparing the elements at index 0 from both list. The comparison stops
only when either the end of the list is reached or corresponding characters in the list are not same.
'''

_list_numbers_1 = [1, 2, 3, 4]
_list_numbers_2 = [1, 2, 3, 4]
if _list_numbers_1 == _list_numbers_2:
    print("lists have same number, type and order of elements")
else:
    print("lists not equal")

_list_numbers_2 += [1]  # _list_numbers_2 += [1] invalid statement and remaining statements will not execute.
                        #  Python interpretor will not throw /show any error.

if _list_numbers_1 == _list_numbers_2:
    print("lists have same number, type and order of elements")
else:
    print("lists not equal")

_list_numbers_1 = [1, 3, 6]
_list_numbers_2 = [1, 4, 7]

if _list_numbers_1 >= _list_numbers_2:
    print("list 1 is greater than list 2")
else:
    print("list1 and list 2 are not equal")

'''
Comparision works as:
Step 1: 1 from _list_numbers_1 is compared with 1 from _list_numbers_1. As they are same, the next two characters are compared.

Step 2: 3 from _list_numbers_1 is compared with 4 from n2. Again they are same, the next two characters are compared.

Step 3: 6 from _list_numbers_1 is compared with 7 from n2. Clearly 3 is smaller than 10. So the comparison n1 > n2 returns False.
'''

_list_strs_1 = ["Java", "Python"]
_list_strs_2 = ["Java", "Python"]

if _list_strs_1 == _list_strs_2:
    print("list 1 elements are greater  than or equal to list 2")
else:
    print("list elements are not greater or equal")

# List Comprehension

_list_squares = [element**2 for element in range(2, 5)]
print(_list_squares)  # [4, 9, 16]

_list_squares = [element**2 for element in range(0, 0)]
print(_list_squares)  # []

