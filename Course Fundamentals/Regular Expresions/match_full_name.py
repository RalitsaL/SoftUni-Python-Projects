import re
text = input()

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
regex_pattern = re.compile(pattern)

matches = re.findall(regex_pattern, text)
print(*matches, sep=" ")