def add(a,b):
    return a+b

result = add(4,5)
print(result)

#no optimal way for add some values
#def add2(list):
#   numbers_add = 0
#    for number in list:
#        numbers_add = numbers_add = number
#    return numbers_add

#result = add2(list)

#using parameter args, can add more parameters this way
def add4(numbers):
    return sum([*numbers])

result2 = add4([3,4,5,6,6,7,7,8,8])
print(result2)

#using parameter args, cant add more parameters this way, parameter arg only can be the last element
def add3(name,*number):
    return f"{name} your sum of number is {sum(number)}"

result = add3("Ker",3,4,5,6,6,7,7,8,8)
print (result)

