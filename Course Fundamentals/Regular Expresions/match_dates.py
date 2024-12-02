import re
all_dates = input()

pattern = r"(?P<Day>\d{2})(?P<separator>[\/.-])(?P<Month>[A-Z][a-z][a-z])\2(?P<Year>\d{4})\b"
# (?P<Day>\d{2})(?P<separator>[\/.-])(?P<Month>[A-Z][a-z][a-z])(?P=separator)(?P<Year>\d{4})\b

pattern_re = re.compile(pattern)
matched_dates = pattern_re.finditer(all_dates)

for date in matched_dates:
    data = date.groupdict()
    print(f"Day: {data['Day']}, Month: {data['Month']}, Year: {data['Year']}")