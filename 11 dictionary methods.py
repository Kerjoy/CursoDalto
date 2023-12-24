"""
KEYS() -> return the keys (useful for iteration)
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

keys_dict = dictionary_1.keys()

print(keys_dict)

for keys_dict in dictionary_1:
    print(keys_dict)
