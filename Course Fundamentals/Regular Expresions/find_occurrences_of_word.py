import re

text = input().lower()
word = input().lower()

pattern = fr"(?i)\b{word}\b"
matches = len(re.findall(pattern, text))
print(matches)