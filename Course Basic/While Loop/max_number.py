from sys import maxsize
max_num = -maxsize


while True:
    command = input()

    if command == "Stop":
        break

    current_num = int(command)

    if current_num > max_num:
        max_num = current_num

print(max_num)


