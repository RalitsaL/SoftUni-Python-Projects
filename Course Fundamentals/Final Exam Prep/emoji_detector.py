import re

my_text = input()
cool_threshold = 1
pattern_digits = r"\d"

matches_digits = re.findall(pattern_digits, my_text)

for match in matches_digits:
    cool_threshold *= int(match)

print(f"Cool threshold: {cool_threshold}")

pattern_emojis = r"(\*{2}|\:{2})([A-Z][a-z]{2,})\1"

matches_emojis = re.finditer(pattern_emojis, my_text)
count_matches = 0

for match in matches_emojis:
    count_matches += 1

print(f"{count_matches} emojis found in the text. The cool ones are:")

matches_emojis_type = re.finditer(r"\*{2}([A-Z][a-z]{2,})\*{2}|:{2}([A-Z][a-z]{2,}):{2}", my_text)

for match in matches_emojis_type:
    countable_word = match.group().replace("*", "").replace(":", "")
    word_threshold = 0
    for letter in countable_word:
        word_threshold += ord(letter)
    if word_threshold >= cool_threshold:
        print(match.group())

