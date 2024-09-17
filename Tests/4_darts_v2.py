name = input()
starting_points = 301
successful = unsuccessful = 0
while True:
    command = input()

    if command == "Retire":
        print(f"{name} retired after {unsuccessful} unsuccessful shots.")
        break

    points = int(input())

    if command == "Double":
        points = points * 2
    elif command == "Triple":
        points = points * 3

    if points > starting_points:
        unsuccessful += 1
        pass

    else:
        starting_points -= points
        successful += 1

    if starting_points == 0:
        print(f"{name} won the leg with {successful} shots.")
        break
