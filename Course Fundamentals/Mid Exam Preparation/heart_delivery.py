neighborhood = list(map(int, input().split("@")))
jump_counter = 0
last_position = 0
while True:

    command = input()
    if command == 'Love!':
        break
    command = command.split(' ')
    jump_counter += 1

    if jump_counter == 1:
        house_index = int(command[1])
    else:
        house_index = int(command[1]) + last_position

    if house_index < len(neighborhood):
        pass
    else:
        house_index = 0

    if neighborhood[house_index] == 0:
        print(f"Place {house_index} already had Valentine's day.")
    else:
        neighborhood[house_index] -= 2
        if neighborhood[house_index] == 0:
            print(f"Place {house_index} has Valentine's day.")

    last_position = house_index

print(f"Cupid's last position was {last_position}.")
neighborhood_new = [i for i in neighborhood if i != 0]

if len(neighborhood_new) == 0:
     print("Mission was successful.")
else:
    print(f"Cupid has failed {len(neighborhood_new)} places.")


