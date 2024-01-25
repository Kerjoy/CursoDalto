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

#using parameter args
def add3(*number):
    return sum(number)

result = add3(3,4,5,6,6,7,7,8,8)
print (result)