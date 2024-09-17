w = int(input())
h = int(input())

cake_size = w * h

while cake_size > 0:
    command = input()

    if command == "STOP":
        print(f"{cake_size} pieces are left.")
        break

    elif command != "STOP":
        command = int(command)
        if command > cake_size:
            print(f"No more cake left! You need {command - cake_size} pieces more.")
        cake_size -= command





