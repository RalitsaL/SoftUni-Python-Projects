wagons = int(input())
my_list = [0] * wagons

while True:
    command = input()

    if command == "End":
        break
    command = command.split()

    if command[0] == "add":
        my_list[-1] += int(command[1])
    elif command[0] == "insert":
        my_list[int(command[1])] += int(command[2])
    elif command[0] == "leave":
        my_list[int(command[1])] -= int(command[2])

print(my_list)

