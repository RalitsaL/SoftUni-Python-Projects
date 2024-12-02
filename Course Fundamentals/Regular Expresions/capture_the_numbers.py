import re
text_input = input()
pattern = r"\d+"
pattern_re = re.compile(pattern)
while text_input:

    matched = pattern_re.finditer(text_input)
    for match in matched:
        print(match.group(), end=" ")
    text_input = input()