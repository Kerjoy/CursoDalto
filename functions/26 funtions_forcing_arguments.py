def phrase(name,last_name,adj):
    return f'Hi {name} {last_name}, you are {adj}'

print1 = phrase("ker","drai","taco")

#forcing arguments in a function with keyword arguments
print2 = phrase(adj = "taco", last_name = "drai", name = "ker")
print(print1)
print(print2)

#default parameters in a optional value, can modify in function calling whith other value

def phrase2(name_1,last_name_1,adj_2 = "without sauce"):
    return f'Hi {name_1} {last_name_1}, you are a taco {adj_2}'

phrase_2_result = phrase2("Ker", "Drai", "Whith sauce")

print(phrase_2_result)