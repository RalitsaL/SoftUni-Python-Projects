def characters_between(first, second):
    list_with_chars = [chr(i) for i in range(ord(first) + 1, ord(second))]
    return list_with_chars


a = input()
b = input()
print(" ".join(characters_between(a, b)))