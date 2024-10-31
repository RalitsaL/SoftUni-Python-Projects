initial_input = input().split()
new_list = []
for word in initial_input:
    first_letter = ""
    for letter in word:

        if letter.isdigit():
            first_letter += letter
    len_first_letter = len(first_letter)
    first_letter = chr(int(first_letter))
    word = list(first_letter + word[len_first_letter:])

    temporally_letter = word[1]
    word[1] = word[-1]
    word[-1] = temporally_letter
    word = "".join(word)
    new_list.append(word)

print(" ".join(new_list))