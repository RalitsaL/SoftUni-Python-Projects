initial_loot = input().split("|")

while True:
    command = input()
    if command == "Yohoho!":
        break

    command = command.split(" ")
    action = command[0]

    if action == "Loot":
        command.remove("Loot")
        # for element in command:
        #     if element in initial_loot:
        #         command.remove(element)
        # command = command[::-1]
        # initial_loot = command + initial_loot
        for element in command:
            if not element in initial_loot:
                initial_loot.insert(0, element)
            else:
                pass


    elif action == "Drop":
        index = int(command[1])
        if index >= len(initial_loot) or index < 0:
            pass
        else:
            initial_loot.append(initial_loot.pop(index))

    elif action == "Steal":
        count = int(command[1])
        if count >= len(initial_loot):
            stollen_items = initial_loot
            initial_loot = []
        else:
            stollen_items = initial_loot[len(initial_loot)-count:]
            initial_loot = initial_loot[:len(initial_loot) - count]
        print(", ".join(stollen_items))


total_length = 0
if len(initial_loot) == 0:
    print(f"Failed treasure hunt.")
else:
    for element in initial_loot:
        total_length += len(element)
    average_gain = total_length/len(initial_loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
