#creating a function that verify if is a prime number
def is_prime_number (num):
    #checking if a number cant divide for any number between 2 and self number -1 
    for i in range(2,num-1):
        #if is a divisible for any number return false and end bucle
        if num%i==0: return False
    #if end the bucle return true because mean is a prime number
    return(True)

#creating a function that return a list with all prime numbers 
def prime_numbers_to(num):
    #making a list for prime numbers
    prime_numbers_list = []
    for i in range(2,num+1):
    #checking if the value is a prime number
        results = is_prime_number(i)
        #in case if true add to the list 
        if results == True: prime_numbers_list.append(i)
    #return the list
    return prime_numbers_list

#create the result calling the function and show it
result = prime_numbers_to(int(input("Give a number for calculation of prime numbers: ")))

print(result)
