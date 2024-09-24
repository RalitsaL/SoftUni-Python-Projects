word = input()
reverse_word = ""

for letter in range(len(word) -1, -1, -1):
    #print(f"{word[letter]}")
    reverse_word += word[letter]

print(reverse_word)