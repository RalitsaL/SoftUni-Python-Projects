import re

my_message = input()
pattern = r"(\^|\*)+([A-Za-z ]{6,})(\^|\*)+(\W*\D*)(\+{1,})(\d{1,}\.\d{1,})\,(\-*\d{1,}\.\d{1,})(\+{1,})"
matches = list(re.finditer(pattern, my_message))

if matches:
    for match in matches:
        print(f"Found {match.group(2)} at coordinates {match.group(6)},{match.group(7)}.")
else:
    print("No valid artifacts found.")