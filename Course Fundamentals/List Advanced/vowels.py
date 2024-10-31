string_input = input()
list_vowels = ["a", "o", "u", "e", "i", "A", "O", "U", "E", "I"]
string_without_vowels = [i for i in string_input if i not in list_vowels]


print("".join(string_without_vowels))