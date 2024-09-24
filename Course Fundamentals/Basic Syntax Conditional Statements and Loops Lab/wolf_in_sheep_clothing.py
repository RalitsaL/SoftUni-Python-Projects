command = input()
words = command.split(", ")
words.reverse()
isfirst = False
counter = 0

for index, word in enumerate(words):
    if word == "wolf":
        if index == 0:
            isfirst = True
        else:
            counter = index

if isfirst:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!")