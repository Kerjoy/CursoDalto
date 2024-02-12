import re

text = "remplacing all vocals for asterisk"

new_text = re.sub("[aeiou]", "*", text)# if i use "aeiou" search exact this, if use instead [aeiou] search any character

print(new_text)