collecting_items = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break

    command = command.split(" - ")
    action = command[0]
    item = command[1]

    if action == "Collect":
        if item in collecting_items:
            pass
        else:
            collecting_items.append(item)
    elif action == "Drop":
        if item in collecting_items:
            collecting_items.remove(item)

    elif action == "Combine Items":
        item = item.split(":")
        item_1 = item[0]
        item_2 = item[1]
        if item_1 in collecting_items:
            collecting_items.insert(collecting_items.index(item_1) + 1, item_2)
    elif action == "Renew":
        if item in collecting_items:
            collecting_items.append(collecting_items.pop(collecting_items.index(item)))

print(", ".join(collecting_items))