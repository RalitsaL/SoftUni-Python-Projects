all_gifts_list = input().split()
while True:
    command = input()

    if command == "No Money":
        break

    output = command.split()

    if "OutOfStock" in command:
        for i in range(len(all_gifts_list)):
            if not all_gifts_list[i]:
                continue
            elif output[1] in all_gifts_list[i]:
                all_gifts_list[i] = None

    elif "Required" in command:
        index = int(output[2])
        if 0 <= index < len(all_gifts_list):
            all_gifts_list[index] = output[1]

    elif "JustInCase" in command:
        all_gifts_list.pop()
        all_gifts_list.append(output[1])

for i in range(len(all_gifts_list)):
    if None in all_gifts_list:
        all_gifts_list.remove(None)

print(" ".join(all_gifts_list))

