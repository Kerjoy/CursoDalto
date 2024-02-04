numbers = [1,2,3,4,5,6,7,8,9]

#creating a function lambda to multiply for 2
multiply_2 = lambda x : x*2

#creating function for checking even number
#def is_even(num):
#    if (num%2==0):
#        return True
    
#using filter with common fuction
#number_even = filter (is_even,numbers)

#same function with lambda functions
number_even = filter(lambda even_number:even_number%2 == 0, numbers)
print(list(number_even))