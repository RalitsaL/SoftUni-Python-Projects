w = int(input())
l = int(input())
h = int(input())

free_space = w * l * h

while free_space > 0:
    command = input()

    if command == "Done":
        print(f"{free_space} Cubic meters left.")
        break
    elif command != "Done":
        command = int(command)
        if free_space < command:
            print(f"No more free space! You need {command - free_space} Cubic meters more.")
        free_space -= command
