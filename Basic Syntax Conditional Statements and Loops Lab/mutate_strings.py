string1 = input()
string2 = input()

for index in range(len(string1)):
    left_part = string2[:index +1]
    right_part = string1[index +1:]
    new_word = left_part + right_part
    if string1 == new_word:
        continue
    else:
        string1 = new_word
        print(new_word)
