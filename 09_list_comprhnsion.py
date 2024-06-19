# -*- coding: utf-8 -*-

# Variables from the task
list1 = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
list2 = [1, 25, 49, 121, 1225, 7921]


# My solution
def square1(x):
    return x ** 2


def is_odd(x):
    return x % 2


# map() and filter()
print('------- map() and filter() -------')
my_list2 = filter(is_odd, map(square1, list1))
print(list(my_list2))

# list comprehension
print('------- List comprehension -------')
my_list2 = [x for x in [x ** 2 for x in list1] if x % 2]
print(list(my_list2))
