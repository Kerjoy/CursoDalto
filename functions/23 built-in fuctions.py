numbers = {2,3,4,5,6,7}

#find max value in the list 
number_max = max(numbers)
print(number_max)

#find minimun value in the list 
number_min = min(numbers)
print(number_min)

#roud to 6 decimals
round_number = 12.3451234
round_number = round(round_number,2)
print(round_number)

#return false -> 0, empty, false, none otherwise if true -> differnt to 0, true, or something return true
result_bool = bool()
result_bool2 = bool("cat")

print (result_bool,result_bool2)

#works cheecking all numbers on iterable object if something is false return false otherwise give true value
result_all = ([0,"true",[344,23]])
print(result_all)

#add all values on iterable
add_total = sum(numbers)
print(add_total)