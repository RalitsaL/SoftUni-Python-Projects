import re

my_text = input()

pattern = r"\s((([a-z0-9]+)[\-\_\.a-z0-9]*)@(([a-z0-9\-]+)(\.([a-z0-9]+))+))"
pattern_re = re.compile(pattern)
matched_emails = pattern_re.finditer(my_text)

for match in matched_emails:
    print(match.group())