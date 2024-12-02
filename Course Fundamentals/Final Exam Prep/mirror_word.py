import re

pair_words = []
all_words = []

initial_text = input()

pattern = r"([#@])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"

matches = re.finditer(pattern, initial_text)

for match in matches:
    if match.group(2) == match.group(3)[::-1]:
        pair_words.append(match.group(2))
        pair_words.append(match.group(3))
    all_words.append(match.group(2))
    all_words.append(match.group(3))

if all_words:
    print(f"{int(len(all_words)/2)} word pairs found!")
else:
    print("No word pairs found!")

if pair_words:
    print("The mirror words are:")
    result = []
    for word in range(0, len(pair_words), 2):
        result.append(f"{pair_words[word]} <=> {pair_words[word+1]}")
    print(", ".join(result))

else:
    print("No mirror words!")