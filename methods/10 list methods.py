"""
LIST - creates a list

LEN - counts the quantity in a list

APPEND - adds an element to a list
INSERT - adds an element to a list at a specific index
EXTEND - adds some elements to a list

POP - deletes an element from a list, requires an index and returns a value
REMOVE - removes an element from a list, specifying a value
CLEAR - deletes all elements from a list

SORT - sorts a list in ascending or descending order
REVERSE - reverses the order of elements in a list
"""

#LIST - create a list
list1 = list(["i", "dont", "known", "was", "here", 1, 2, 3, True])

#LEN - counts the quantity in a list
print(f"numero de elementos{len(list1)}")

#APPEND - adds an element to a list
list1.append("michi")
print(list1)

#INSERT - adds an element to a list at a specific index
list1.insert(0,"michi")
print(list1)

#EXTEND - adds some elements to a list
list1.extend(list1)
print(list1)

#POP - deletes an element from a list, requires an index and returns a value
print(list1.pop(0))

#REMOVE - removes an element from a list, specifying a value
list1.remove("here")
print(list1)

#CLEAR - deletes all elements from a list
list1.clear()
print(list1)

#SORT - sorts a list in ascending or descending order
#REVERSE - reverses the order of elements in a list