#!/usr/local/bin/python
# coding=UTF-8
######################################################################################
# Created by Sahoo, Prasanta K
# Copyright © 2021 Prasanta K. Sahoo. All rights reserved.
#
# Source : https://docs.python.org/3.10/tutorial/datastructures.html
######################## What You Would Find Here
# 1.0 - The list, 1.2 - List As stack (last-in, first-out), 1.3 - List As Queues (“first-in, first-out”),
# 1.4 - List Comprehensions (Different ways to create list), 1.5 - List Comprehensions (Different ways to create list),
# 1.6 - Nested List Comprehensions (Different ways to create list)
# 2.0 - Tuples and Sequences, 3.0 - Set, 4.0 - Dictionaries
######################################################################################
from collections import deque

'''
1.0 - The list
'''
def listExample():
    print("---------- listExample -----------")
    data_list = ["data1", "data2", "data3", "data4", 1, 12.4]
    print("Initial state ", data_list)
    data_list.sort()
    print("After sort ", data_list)

'''
1.2 - List As stack (last-in, first-out)
'''
def listAsStacks():
    print("\n---------- listAsStacks -----------\n")
    data_list = [2,3,4,5]
    print("At initial ", data_list)
    data_list.append(1001)
    print("After Append ", data_list)
    data_list.pop() # Last 1001 added and first to out using pop
    print("After Pop", data_list)

'''
1.3 - List As Queues (“first-in, first-out”)
Warning : "lists are not efficient for this purpose. While appends and 
pops from the end of list are fast, doing inserts or pops from the beginning 
of a list is slow (because all of the other elements have to be shifted by one"

Collections.deque which was designed to have fast appends and pops from both ends
'''
def listAsQueues():
    print("\n---------- listAsQueues -----------\n")
    data_list = [2,3,4,5]
    print("At initial ", data_list)
    data_as_queue = deque(data_list)
    print("After data_as_queue ", data_as_queue)
    data_as_queue.append(1002)
    print ("After append(1002) ", data_as_queue)
    print("The popleft value ", data_as_queue.popleft())
    print("After  popleft data_as_queue ", data_as_queue)
    print("The pop value ", data_as_queue.pop()) #
    print("After pop data_as_queue ", data_as_queue)


'''
1.4 - List Comprehensions (Different ways to create list)
- A Lambda Function is an anonymous function
'''
def listComprehensionsExample():
    data_list = []
    for x in range(5):
        data_list.append(x)
    print("Data to list in type 1 ", data_list)
    data_list = list(map(lambda y: x , range(5)))
    print("Data to list in type 2 ", data_list)
    data_list = [x for x in range(5)]
    print("Data to list in type 3 ", data_list)
    data_list = [str(1.5 + i) for i in range(1, 6)]
    print("Data to list in type 4 ", data_list)

'''
1.5 - List Comprehensions (Different ways to create list)
- A Lambda Function is an anonymous function
'''
def listComprehensionsExample():
    data_list = []
    for x in range(5):
        data_list.append(x)
    print("Data to list in type 1 ", data_list)
    data_list = list(map(lambda y: x , range(5)))
    print("Data to list in type 2 ", data_list)
    data_list = [x for x in range(5)]
    print("Data to list in type 3 ", data_list)
    data_list = [str(1.5 + i) for i in range(1, 6)]
    print("Data to list in type 4 ", data_list)


'''
1.6 - Nested List Comprehensions (Different ways to create list)
'''
def nestedListComprehensionsExample():
    data_list = []
    data_list.append([1,3])
    data_list.append([1, 4])
    print("Data to list in type 1 ", data_list)
    del data_list[:] # del statement
    for x in range(4):
        for y in range(4):
            data_list.append([x, y])
    print("Data to list in type 2 ", data_list)
    del data_list[:]  # del statement
    data_list = [[1,2],[3,4],[5,6]]
    data_list_new = [[row[i] for row in data_list] for i in range(2)]
    print("Data to list in type 3 ", data_list_new)

'''
2.0 - Tuples and Sequences
Tuple consists of a number of values separated by commas
list, tuple, range are sequence data types 
https://docs.python.org/3.10/library/stdtypes.html#typesseq
Tuples are immutable where as lists are mutable.
'''
def tupleExample():
    tuple_data = 12, 323, 'data3', "data4"
    print("tuple_data at 1 ", tuple_data[1])
    tuple_data_new = 'new_data', tuple_data
    print("nested tuple_data_new  ", tuple_data_new) # Nested
    #TypeError: 'tuple' object does not support item assignment
    #Tuples are immutable , below can not be done
    #tuple_data[2] = 89
    tuple_data_array = [1,2,3], [5,6,7] # They can have array
    x,y = tuple_data_array
    print("This is called Appropriately enough, sequence unpacking", x, y)

'''
3.0 - Set
a. set is an unordered collection with no duplicate elements
b. You can use union, intersection, difference, and symmetric difference
c. Curly braces (not for empty set) or the set() can be used for creating the set 
'''
def setExample():
    set_with_braces = {'data1', 'data2', 'data3', 1}
    print(" Set with curly braces  ", set_with_braces)

    set_with_functions = set('1sasdasfd') # class set([iterable]) , class frozenset([iterable])
    print(" Set with function  ", set_with_functions)
    set_with_functions_2 = set([212,2121,2121,'wwqrqwr'])
    print(" Set with function 2 ", set_with_functions_2)
    print(" Set with function 2 ", set_with_functions - set_with_functions_2)
    for x, val in enumerate(set_with_functions_2):
        print(" For loop ", x, val)

    # Two sqence at a time
    for x, y in zip(set_with_braces, set_with_functions_2):
        print('Combine sequence data {0} -  {1}'.format(x, y))
''' 
4.0 - Dictionaries
https://docs.python.org/3.10/library/stdtypes.html#typesmapping
a. dictionary as a set of key: value pairs
b. You can use union, intersection, difference, and symmetric difference
c. Curly braces (not for empty set) or the set() can be used for creating the set 
'''
def dictionariesExample():
    dictionary_with_braces = {'data1': 12, 'data2':34, 'data3':55}
    print(" Dictionarie with curly braces  ", dictionary_with_braces)
    dictionary_with_braces["data4"] = "string_value"
    print(" Dictionarie after one more data  ", dictionary_with_braces)
    print(" All the keys  ", list(dictionary_with_braces))
    print(" All the keys  ", 'data5' in dictionary_with_braces)
    print(" All the keys  ", 'data5' not in dictionary_with_braces)

    dictionary_with_const = dict([('data1', 12), ('data2', 11), ('data3', 22)])
    print(" Dictionarie with constructor  ", dictionary_with_const)
    for key, val in dictionary_with_const.items():
        print("For loop ", key, val)

if __name__ == "__main__":
    #listExample()
    #listAsStacks()
    #listAsQueues()
    #listComprehensionsExample()
    #nestedListComprehensionsExample()
    #tupleExample()
    setExample()
    #dictionariesExample()
