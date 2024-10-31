my_list = [0] * 11

while True:
    command_initial = input()
    if command_initial == "End":
        break

    command = command_initial.split("-")
    position = int(command[0])
    note = command[1]
    my_list.pop(position)
    my_list.insert(position, note)


result = [i for i in my_list if i != 0]
print(result)