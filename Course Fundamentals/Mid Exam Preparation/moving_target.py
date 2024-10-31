my_list = list(map(int, input().split()))

while True:
    command = input()
    if command == 'End':
        break

    command = command.split(' ')
    action = command[0]
    index = int(command[1] if 0 <= int(command[1]) < len(my_list) else -1)

    value = int(command[2])

    if action == "Shoot":
        if index > -1:
            my_list[index] -= value
            if my_list[index] <=0:
                my_list.pop(index)
    elif action == "Add":
        if index > -1:
            my_list.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        if index > -1:
            if 0 <= index + value <= len(my_list) and 0 <= index - value <= len(my_list):
                my_list.pop((index + value))
                my_list.pop(index)
                my_list.pop((index - value))
            else:
                print("Strike missed!")

print("|".join(map(str, my_list)))
