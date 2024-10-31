my_list = list(map(int, input().split()))

while True:
    command = input()

    if command == "end":
        break

    command = command.split()
    action = command[0]


    if action == "decrease":
        for i in range(len(my_list)):
            my_list[i] -= 1
    elif action == "swap":
        index1 = int(command[1])
        index2 = int(command[2])
        my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    elif action == "multiply":
        index1 = int(command[1])
        index2 = int(command[2])
        my_list[index1] = my_list[index1] * my_list[index2]

print(", ". join(map(str, my_list)))