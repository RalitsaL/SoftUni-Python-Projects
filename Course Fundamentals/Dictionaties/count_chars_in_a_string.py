string = input().replace(" ", "")
count = 0
my_dict = dict.fromkeys(string, count)
for letter in string:
    if letter in string:
        my_dict[letter] += 1

for letter in my_dict:
    print(f"{letter} -> {my_dict[letter]}")