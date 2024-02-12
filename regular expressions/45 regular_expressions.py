import re

text = '''Welcome to the Python Text Adventure Game!
In this game, you will embark on an epic journey through the mysterious lands of Pythonia.
Are you ready to begin 123 123. your adventure?
Please enter 'yes' or 'no':
ab bb'''

result = re.search("game", text) #return the first match
results = re.findall("game", text) #return the all matchs cand add flags=

#\d search numbers 0-9
#\D search not numbers 0-9, In most cases, uppercase letters do the opposite

#result = re.findall(r"\d",text)
result = re.findall(r"\D",text)

#\w search all alphanumeric match [a-z A-Z 0-9 _]
#\W search not alphanumeric match [a-z A-Z 0-9 _]

#result = re.findall(r"\w",text)
result = re.findall(r"\W",text)

#\s search all blank spaces, spaces, tabs, line break
#\S search not blank spaces, spaces, tabs, line break
result = re.findall(r"\s",text)

#. search all without line break
#/n search all line breaks
result = re.findall(r"\n",text)

#/ cancel special characters, canceling the function of the period, and searching for dots
result = re.findall(r"\.",text)

#creating a string with search a number, next a dot and space
result = re.findall(r"\d\.\s",text)

#search the start of line
#^ search start of line
 #with this flag is multiline with .IGNORECASE ignore upper and lower case
result = re.findall(r'^Welcome',text,flags=re.M)

#$ search end of line
result = re.findall(r'Pythonia.$',text,flags=re.M)

#{n} groups search n quantity of value to left
result = re.findall(r'\d{3}\s',text)

#{n,m} range search n quantity min and m quantity max of value to left
result = re.findall(r'\d{1,4}\s',text)
result = re.findall(r'ab{2,4}',text)
result = re.findall(r'(ab){1,2}',text)
result = re.findall(r'[ab]{2}',text) #return "aa", "ab", "ba" y "bb"

# | is this OR on regular expresions
result = re.findall(r'Welcome|Game',text)

print(result)