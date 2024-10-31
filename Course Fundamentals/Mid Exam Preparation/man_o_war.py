status_pirate_ship = list(map(int,input().split(">")))
status_warship = list(map(int,input().split(">")))
max_health_capacity = int(input())
lose_or_win = False
while True:
    command = input()
    if command == "Retire":
        break

    command = command.split(" ")
    action = command[0]

    if action == "Fire":
        index = int(command[1])
        if 0 <= index < len(status_warship):
            damage = int(command[2])
            if damage >= status_warship[index]:
                print(f"You won! The enemy ship has sunken.")
                lose_or_win = True
                break
            else:
                status_warship[index] -= damage
        else:
            pass


    elif action == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if 0 <= start_index <= end_index < len(status_pirate_ship):
            for i in range(start_index, end_index + 1):
                if damage >= status_pirate_ship[i]:
                    lose_or_win = True
                else:
                    status_pirate_ship[i] -= damage
        else:
            pass
        if lose_or_win:
            print(f"You lost! The pirate ship has sunken.")
            break

    elif action == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(status_pirate_ship):
            if health + status_pirate_ship[index] >= max_health_capacity:
                status_pirate_ship[index] = max_health_capacity
            else:
                status_pirate_ship[index] += health
        else:
            pass

    elif action == "Status":
        need_repair_if_lower_than = 0.2 * max_health_capacity
        count = len([i for i in status_pirate_ship if i < need_repair_if_lower_than])
        print(f"{count} sections need repair.")

if not lose_or_win:
    print(f"Pirate ship status: {sum(status_pirate_ship)}\nWarship status: {sum(status_warship)}")