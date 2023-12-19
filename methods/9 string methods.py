"""
DIR - Return the list of attributes from past object

UPPER - Convert to uppercase
LOWER- Convert to lowcase
CAPITALIZE - First in uppercase

FIND - method find the first coincidence of specific value, else return 1
INDEX - method find the first coincidence of specific value, else rise a Exception

ISNUMERIC - if is a number return True
ISALPHA - is is alpha-numeric return True

ENDSWITH - verify if a string end with
STARTSWITH - verify if a string atart with

replace - replace a value with other
split - split a parameter
"""

string1 = "Hi user"
string2 = "give taquito"

#examples of use methods 
result = "hi is my first pre built methods in python".upper()
result2 = string1.lower()

#print(dir(string1)) print atrib of object string

print(f"first string {result} second string {result2}")

#capitalize a phrase, convert all lowercase except first
first_letter_upper = string2.capitalize()

print (first_letter_upper)

#find a string in other string, if not have any coincidence return -1

q_find = result.find(("my").upper())

print(q_find)