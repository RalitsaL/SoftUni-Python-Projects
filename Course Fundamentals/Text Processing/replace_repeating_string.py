my_text = input()
short_version = list(my_text[0])

for index in range(1, len(my_text)):
    current = my_text[index]
    if current != my_text[index-1]:
        short_version.append(current)

print("".join(short_version))
