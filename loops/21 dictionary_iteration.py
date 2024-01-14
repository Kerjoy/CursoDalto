dictionary1 = {"name": "mr. ker",
               "last name": "drai",
               "number": 1234,
               "empty field": "not so much empty"}


for key in dictionary1: #this way only get keys
    print(key)
    
for value in dictionary1.items(): #this way get al dictionary 
    print(value)
    
    
fruits = ["banana", "apple", "plum", "pear", "orange", "dragon fruit", "peach"]

for fruit in fruits:
    if fruit == "plum": #not this one 
        continue #continue skip the iteration
    
    print(f"i like this fruit: {fruit}")
    
    if fruit == "dragon fruit":
        break
else: 
    print("terminaron las frutas") 
    
#iteration over string

random_string = "The melody of stars whispers in the cosmic symphony."

for character in random_string:
    print(character)
    
#iteration and multiplication on list 
numbers = [1,2,3,4,5,6,7,8,9,10]
numbers_multiply = list()

for number in numbers:
    numbers_multiply.append(number*2)
    
print(numbers_multiply)

#iteration and multiplication on list, but only one line, math expresion next for estructure
numbers_multiply_2 = [numbers_2 * 2 for numbers_2 in numbers_multiply]

print(numbers_multiply_2)