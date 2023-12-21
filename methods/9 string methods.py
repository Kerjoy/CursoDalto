"""
DIR - Return the list of attributes from past object ( FUNCTION)

UPPER - Convert to uppercase
LOWER- Convert to lowcase
CAPITALIZE - First in uppercase

FIND - method find the first coincidence of specific value, else return 1
INDEX - method find the first coincidence of specific value, else rise a Exception

ISNUMERIC - if is a number return True
ISALPHA - is is alpha-numeric return True

COUNT - returns the number of ocurrences of a sub-string in the given string
LEN - returns the total of characters in the given string (FUNCTION)

ENDSWITH - verify if a string end with
STARTSWITH - verify if a string atart with

REPLACE - replace a value with other
SPLIT - split a parameter

LIST - create a list

ALL METHOS ARE FUNCTIONS BUT NOT ALL FUNCTIONS ARE METHODS 
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

#find a string in other string, if not have any coincidence return a exception

#r_except= result.index("my".upper())

#print (r_except)

# isnumeric - if is a number return True
num = "555"
print(num.isnumeric())
# isalpha - is is alpha-numeric return True
alp = "probealpha"
print(alp.isalpha())

sentence3 = "only need this string for practice 1111"
sentence4 = "this, emulates, a csv, file, or something, like that"

#COUNT - returns the number of ocurrences of a sub-string in the given string
print(sentence3.count("1"))
#LEN - returns the total of characters in the given string
print(len(sentence4))

#endswhith - verify if a string end with
end_w = "hi, is a program exercise"
print(end_w.endswith("exercise"))
#startwith - verify if a string atart with
start_w = "only have a bit time for this"
print(start_w.startswith("have"))

#replace - replace a value with other
sentence1 = "only need this string for practice 1111"
print(sentence1.replace("1111","success"))
#split - split a parameter
sentence2 = "this, emulates, a csv, file, or something, like that"
print(sentence2.split(","))