def phrase(name,last_name,adj):
    return f'Hola {name} {last_name}, you are {adj}'

print1 = phrase("ker","drai","taco")

#forcing arguments in a function with keyword arguments
print2 = phrase(adj = "taco", last_name = "drai", name = "ker")
print(print1)
print(print2)