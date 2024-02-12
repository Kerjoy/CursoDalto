import re

text = "this a example of webpage https://www.exaple.com"

pattern = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.findall(pattern,text)

print(result)
