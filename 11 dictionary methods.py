"""
keys() -> return the keys (useful for iteration)
get() -> return the value of a key
clear() -> deletes all elements
pop() -> deletes a element
items() -> for dict iteration
"""

dictionary_1 = {
    "name" : 'gear',
    "material" : 'iron',
    "prices" : '10'
}

#return a object dict_item
keys_dict = dictionary_1.keys()
print(keys_dict)

for keys_dict in dictionary_1: # iteration on dictionary
    print(keys_dict) #print keys 
    print(dictionary_1.get(keys_dict)) #print fields of dictionary, dont rise exceptions
    
#deleting all dictionary
#dictionary_1.clear()

#deleting elements of dictionary with key value, dictionary_1.pop("name","material")
dictionary_1.pop("name")

#getting a element dict_items iterable
dictionaru_iter = dictionary_1.items()

print(dictionary_1)