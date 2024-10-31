my_list = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break

    command = command.split(" ")
    action = command[0]
    item = command[1]

    if action == "Urgent":
        if item in my_list:
            pass
        else:
            my_list.insert(0, item)
    elif action == "Unnecessary":
        if item in my_list:
            my_list.remove(item) #tuk moje i da ima drama
        else:
            pass
    elif action == "Correct": #tuk ne raboti
        if item in my_list:
            my_list[my_list.index(item)] = command[2]
        else:
            pass
    elif action == "Rearrange":
        if item in my_list:
            my_list.append(my_list.pop(my_list.index(item)))


print(", ".join(my_list))