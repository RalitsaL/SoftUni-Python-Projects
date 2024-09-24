word = input()
my_list = []

for i, letter in enumerate(word):
    check = letter.isupper()
    if check:
        my_list.append(i)

print(my_list)