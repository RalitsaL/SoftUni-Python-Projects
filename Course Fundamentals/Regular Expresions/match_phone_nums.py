import re

number = input()
pattern = r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b"

numbers = re.findall(pattern, number)
print(*numbers, sep=", ")