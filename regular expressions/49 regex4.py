import re

email = "example@example.com"

pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.match(pattern,email)

if result:
    print("Valid Email")
else:
    print("No valid Email")