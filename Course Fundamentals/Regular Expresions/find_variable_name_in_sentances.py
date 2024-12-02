import re

text = input()

pattern_ = r"(?<=\b\_{1})[a-zA-Z]+\b"
pattern = re.compile(pattern_)
matches = pattern.findall(text)

print(",".join(matches))