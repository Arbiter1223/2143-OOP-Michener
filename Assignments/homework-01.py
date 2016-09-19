"""
Name: Cory Michener
Email: Arbiter1223@live.com
Assignment: Homework 1 - Lists and Dictionaries
Due: September 19 @ 1:00 P.M.
"""

# 1.1 Basics
# A: What would Python print?

a = [1, 5, 4, 2, 3]
print (a[0], a[-1])
# Prints "1 3"
# a[0] represents the first element in the list, which currently contains 1
# a[-1] refers to the last element in the list, in this case, 3

a[4] = a[2] + a[-2]
print (a)
# Prints "[1, 5, 4, 2, 6]"
# The fourth element is first set to the sum of the second element
# and the element second from the end.
# Then the entire list is printed.

print (len(a))
# Prints "5"
# It prints the number of elements in the list, which is currently 5

print (4 in a)
# Prints "True"
# Since the value 4 is in the list, it returns True

a[1] = [a[1], a[0]]
print (a)
# Prints "[1, [5, 1], 4, 2, 6]"
# It sets the second element to a child list that contains
# the former second and first elements of the parent list



# 1.2 List Methods
# B: Write a function that removes all instances of an element from a list

"""def remove_all
Function: Removes all instances of a given element from a list
Example: exList1 = [1, 2, 2, 3]
Usage: remove_all(2, exList1)
Result: [1, 2, 2, 3]"""
def remove_all(e, list):
    while e in list:
        list.remove(e)

# C: Write a function that takes two values (x and y) and a list and adds as many y's to the end
# of the list as there are x's. (Note: do not use the build-in function count)

"""def add_to_end
Function: Adds a number to the end of a list by the number of instances of a certain element
in the list
Example: exList2 = [1, 2, 2, 3]
Usage: add_to_end(2, 6, exList2)
Result: [1, 2, 2, 3, 6, 6]"""
def add_to_end(x, y, list):
    i = 0
    l = len(list)
    while i < l:
        if list[i] == x:
            list.append(y)
        i += 1

# 1.3 Slicing
# D: What would Python print?

a = [3, 1, 4, 2, 5, 3]
print (a[:4])
# Prints: "[3, 1, 4, 2]"
# It prints from the beginning of the list to the 4th element

print (a)
# Prints: "[3, 1, 4, 2, 5, 3]"
# The entire list is printed

print (a[1::2])
# Prints: "[1, 2, 3]"
# It prints the first element and then prints elements on an interval of 2

print (a[4:2])
# Prints: "[]"
# It won't print going backwards in a list

print (a[1:-2])
# Prints: "[1, 4, 2]"
# Starts with the second element and prints up to, but not including, the element 2 from the end

print (a[::-1])
# Prints: "[3, 5, 2, 4, 1, 3]"
# Prints the list backwards

# 1.4 For loops
# E: Write a function that reverses Python lists in place

"""def reverse_list
Function: Reverse a list
Example: exList3 = [1, 2, 2, 3, 1, 9, 9, 6]
Usage: reverse_list(exList3)
Results: [6, 9, 9, 1, 3, 2, 2, 1]"""
def reverse_list(list):
    l = len(list)
    for i in range(l//2):
        list[i], list[l -1 - i] = list[l -1 - i], list[i]
    print (list)
# Source: http://xahlee.info/comp/in-place_algorithm.html

# F: Write a function that rotates the elements of a list by k.

"""def rotate
Function: Rotates elements from front of list to end k times
Example: exList3 = [1, 2, 2, 3, 1, 9, 9, 6]
Usage: rotate(exList3, 4)
Results: [1, 9, 9, 6, 1, 2, 2, 3]"""
def rotate(list, k):
    for i in list:
        if k > 0:
            temp = list[0]
            list.append(temp)
            del(list[0])
            k -= 1
    print (list)

# 2 Dictionaries
superbowls = {'joe montana':4, 'tom brady':3, 'joe flacco':0}
superbowls['peyton manning'] = 1
superbowls['joe flacco'] = 1

# H: What would Python print?
print('colin kaepernick' in superbowls)
# Prints: "False"
# The guy whom I cannot pronounce his name is not in the dictionary

print (len(superbowls))
# Prints: "4"
# There are 4 entries in the dictionary

print (superbowls['peyton manning'] == superbowls['joe montana'])
# Prints: "False"
# The key for Peyton manning is 1, and the key for Joe Montana is 4
# 1 !=4, hence it is False

superbowls[('eli manning', 'giants')] = 2
print (superbowls)
# Prints: {('eli manning', 'giants'): 2, 'tom brady': 3, 'joe flacco': 1, 'peyton manning': 1, 'joe montana': 4}
# "('eli manning', 'giants')" is considered to be a single entry in the dictionary, and the key for that entry is 2

superbowls[3] = 'cat'
print (superbowls)
# Prints: {3: 'cat', 'tom brady': 3, 'peyton manning': 1, 'joe montana': 4, 'joe flacco': 1, ('eli manning', 'giants'): 2}
# Adds an entry '3' with a key 'cat'

superbowls[('eli manning', 'giants')] = superbowls['joe montana'] + superbowls['peyton manning']
print (superbowls)
# Prints: {3: 'cat', 'peyton manning': 1, 'joe montana': 4, 'joe flacco': 1, ('eli manning', 'giants'): 5, 'tom brady': 3}
# The key for joe montana is 4, and the key for peyton manning is 1
# So it assigns the key 5 (4+1) to eli manning and giants

# superbowls[['steelers', '49ers']] = 11
# print (superbowls)
# Prints error message:
# Traceback (most recent call last):
#   File "c:\2143-OOP-Michener\Assignments\homework-01.py", line 163, in <module>
#     superbowls[['steelers', '49ers']] = 11
# TypeError: unhashable type: 'list'

# I: Given a dictionary, replace all occurences of x as the values with y

"""def replace_all_dict
Function: Takes all occurrences of x as the value with y
Example: d = {1: {2:3, 3:4}, 2:{4:4, 5:3}, 3:3}
Usage: replace_all_dict(d, 3, 1)
Results: d = {1: {2:3, 3:4}, 2:{4:4, 5:3}, 3:1}"""
def replace_all_dict(dict, x, y):
    for k in dict.keys():
        if dict[k] == x:
            dict[k] = y
    print (dict)        

# J: Delete all occurences of a value without iterating through the dictionary

"""def rm
Function: Remove all occurances of value in dictionary
Example: d = {1:2, 2:3, 3:2, 4:3}
Usage: rm(d,2)
Results: {1: 2, 3: 2, 4: 3}"""
def rm(mydict, x):
    for k in list(mydict.keys()):
        if k == x:
            del mydict[k]
# Source: http://stackoverflow.com/questions/5384914/how-to-delete-items-from-a-dictionary-while-iterating-over-it

