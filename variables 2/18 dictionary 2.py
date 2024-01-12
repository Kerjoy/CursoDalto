dictionary_1= dict(name="ker", lastname="joy")

dictionary_2 = {
    'name': "ker",
    'lastname': "joy"
}

#the tuples can be keys, and the lists cant be keys, can use it if use frozen set, need hasheable data
dictionary_1 = {frozenset(["ker","joy"]):"jajas"}


dictionary_2 = dict.fromkeys("ABCDE","12345") # this way have a:12345 , b :12345 so on
#if i try use a list instead for only keys get a dictionary empty (none values)
dictionary_2 = dict.fromkeys(["name","lastname","number"])

dictionary_3 = dict.fromkeys(["data1","data2"])#first value its a iterable, and second value its a value for keys
#overwriting values
dictionary_3 = dict.fromkeys(["data1","data2"],"idontknow")

print(dictionary_3)