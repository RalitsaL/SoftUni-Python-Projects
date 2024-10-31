sequense_elements = input().split()
counter_trys = 0

while True:
    command = input()

    if command == "end":
        break

    command = command.split()
    counter_trys += 1
    index_1 = int(command[0])
    index_2 = int(command[1])

    if index_1 < 0 or index_1 >= len(sequense_elements) or \
            index_2 >= len(sequense_elements) or index_2 < 0 or index_1 == index_2:
        middle = int(len(sequense_elements) / 2)
        sequense_elements.insert(middle, f"-{counter_trys}a")
        sequense_elements.insert(middle + 1, f"-{counter_trys}a")
        print("Invalid input! Adding additional elements to the board")
    else:
        if sequense_elements[index_1] == sequense_elements[index_2]:
            print(f"Congrats! You have found matching elements - {sequense_elements[index_1]}!")
            sequense_elements = [i for i in sequense_elements if i not in (sequense_elements[index_1], sequense_elements[index_2])]

        elif sequense_elements[index_1] != sequense_elements[index_2]:
            print("Try again!")

        if len(sequense_elements) == 0:
            print(f"You have won in {counter_trys} turns!")
            break

if len(sequense_elements) > 0:
    print(f'Sorry you lose :(\n{" ".join(sequense_elements)}')