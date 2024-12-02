import re

my_string = input()

pattern = r"(/|=)([A-Z][A-Za-z]{2,})\1"

matches = re.finditer(re.compile(pattern), my_string)

print("Destinations:",", ".join(matches.group(2) for matches in matches))

travel_points = 0

matches_length = re.finditer(re.compile(pattern), my_string)
for match in matches_length:
    travel_points += len(match.group(2))

print("Travel Points:",travel_points)
