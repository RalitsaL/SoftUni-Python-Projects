my_string = input().upper()
only_uniques = []

for symbol in my_string:
    if symbol.isdigit():
        pass
    else:
        if symbol not in only_uniques:
            only_uniques.append(symbol)

print(f"Unique symbols used: {len(only_uniques)}")

new_string = []

part_to_repeat = ""
repetitions = ""
for index in range(len(my_string)):
    if not my_string[index].isdigit():
        part_to_repeat +=  my_string[index]
    if  my_string[index].isdigit():
        if index + 1 < len(my_string) and my_string[index + 1].isdigit():
            repetitions += my_string[index]
        else:
            repetitions += my_string[index]
            new_string.append(part_to_repeat*int(repetitions))
            part_to_repeat = ""
            repetitions = ""
print("".join(new_string))
