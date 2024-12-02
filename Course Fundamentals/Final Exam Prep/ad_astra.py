import re
text_string = input()

pattern = r"(\#|\|)([a-zA-Z ]+)\1(\d{2}\/\d{2}\/\d{2})\1([0-9]|[1-9][0-9]{1,3}|10000)\1"

total_calories = 0
matches_calories = re.finditer(pattern, text_string)
for match in matches_calories:
    total_calories += int(match.group(4))

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
matches = re.finditer(pattern, text_string)

for match in matches:
    print(f"Item: {match.group(2)}, Best before: {match.group(3)}, Nutrition: {match.group(4)}")