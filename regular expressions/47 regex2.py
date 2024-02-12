import re

#the string the search the patterns
text = "The date is 23/06/2021 and the phone is +1-555-555-5555"

#the pattern to find
pattern = r"\d{2}/\d{2}/\d{4}"

#pattern replacement
replacement = "hidden date"

new_text = re.sub(pattern,replacement,text)

print(new_text)