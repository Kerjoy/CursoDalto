#
#can modify
#you must put in parentheses []
list = ["Juan","Ker",True,1.73]

#dif between list, is cant modify
#you must put in parentheses ()
tuple = ("Juan","Ker",True,1.73)


#correct
list[2] = "Taquito"

#incorrect
#tuple[2] = "Taquito"

#print(list[2])

#creating a set
#you must put in parentheses {}
#can modify but not have access from index
#set do not allow duplicates
set = {"name", "last name", True, 1.73}

#creating a dictionary (dict)
#dictionary can use a key to get value of any storage variable
# the structure is key : value and comma-separated, and repeat, the last items no longer need a comma
dictionary = {
    'name' : "Ker",
    'pet' : "cat",
    'bool' : True,
    'age' : 27
}

print (dictionary['age'])
