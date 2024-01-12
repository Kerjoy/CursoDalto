#making a set

conjunto_set =set(["data 1","data 2"])

print(conjunto_set)

#put a set on other set
conjunto1 = frozenset(["dato 1", "data 2"])
conjunto2 = {conjunto1,"dato 3"}
print(conjunto2)

#teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#checking if is a subset conjunto1 from conjunto2
result = conjunto2.issubset(conjunto1)
result = conjunto2 <= conjunto1 # other way for comparison subset

print(result)

#checking if is a superset conjunto1 from conjunto2
result = conjunto2.issuperset(conjunto1)
result = conjunto2 > conjunto1 # other way for comparison subset

#check if it ever has the same number, if have a coincidence returns false, otherwise returns true
result = conjunto2.isdisjoint(conjunto1)
print(result)