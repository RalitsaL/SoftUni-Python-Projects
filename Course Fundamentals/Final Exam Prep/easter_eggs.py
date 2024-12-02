import re

my_message = input()
pattern = r"([@#]+)([a-z]{3,})([@#]+)(\W*\D*)([\/]+)(\d+)([\/]+)"
matches = re.finditer(pattern, my_message)


for match in matches:
    print(f"You found {match.group(6)} {match.group(2)} eggs!")