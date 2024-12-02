import re

my_text = input()

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

pattern_re = re.compile(pattern)

matched_nums = pattern_re.finditer(my_text)

for item in matched_nums:
    print(item.group(), end = " ")