key = int(input())
letters = int(input())

for letter in range(letters):
    letter = ord(input())
    print(chr(letter + key), end="")