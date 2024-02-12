import re

#detecting a phone number and hidding it

text = "Hi mi name is idk, my phone number is: +54 11 4321-4654"

pattern = r'\+\d{2}\s\d{2}\s\d{4}\-\d{4}'

replacing = re.sub(pattern,"(hidden number)",text)

print (replacing)