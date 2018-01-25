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

