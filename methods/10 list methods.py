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

#EXTEND - adds an iterable
list1.extend(list1)
print(list1)

#POP - deletes an element from a list, requires an index and returns a value
print(list1.pop(0))
print(list1.pop(-1))#deletes last element from the list -2 prev last and so on

#REMOVE - removes an element from a list, specifying a value otherwise rise a exception
list1.remove("here")
print(list1)

#CLEAR - deletes all elements from a list
list1.clear()
print(list1)

#SORT - sorts a list in ascending or descending order
number_list = ([2,3,5,6,8,0,102,24,45,123, True, True, False, False]) # dont work with strings
number_list.sort()
print(f"Demostration of sort method for a list {number_list}")
number_list.sort(reverse=True)
print(f"Demostration of sort method with attribute reverse for a list {number_list}")

#REVERSE - reverses the order of elements in a list without sort
number_list.reverse()
print(f"reversing a list {number_list}")

search_element = number_list.index(2) # search on a reversed list else rise a exception
print(search_element)

search_element_in_set = set(["1","2"]) #defines a set

se1 = search_element.__index__("1") #set not have a index method