animals = ["cat","dog","parrot","cocodrile","fish"]
numbers = [1,2,3,4,5]

#iterarion of animal list
for animal in animals:
    print(f"current animal in iteration: {animal}")
    
print("----------------")

#iteration over all number and multiply
for number in numbers:
    result = number * 10
    print(result)
    
print("----------------")
    
#with zip can have iterarion in more than one list
for number,animal in zip(numbers,animals):
    print(number,animal)
    
print("----------------")
    
#with range instead a iterable object
for number_range in range(1,11):
    print(number_range)
    
print("----------------")

#incorrect way for iteration on list
#for num in range(len(numbers)):
#    print(numbers[num])
    
#correct way for iteration on list, enumarates make a tuple with index over each element
for num in enumerate(numbers):
    #print(type(num))
    index = num[0]
    value = num[1]
    print(f"index: {index} value: {value}")
    
print("----------------")

#upacking all values on loop, first index and after the value
for i,num in enumerate(numbers):
    print(i," ",num)

#upacking all values on loop, first index and after the value
for i,num in enumerate(numbers):
    print(i," ",num)
else:
    print("loop end")
    
#all works same way for tuples or list