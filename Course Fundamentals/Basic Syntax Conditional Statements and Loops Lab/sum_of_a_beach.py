command = input().lower()
words = ["Sand", "Water", "Fish", "Sun"]
counter = 0

for word in words:
    if word.lower() in command:
        count_of_word = command.count(word.lower())
        counter += count_of_word

print(counter)