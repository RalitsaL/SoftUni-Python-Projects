current_energy = 100
current_coins = 100
gained_energy = 0

events = input().split("|")
flag = True

for elements in events:
    event = elements.split("-")
    event_or_ingredient = event[0]
    number = int(event[1])

    if event_or_ingredient == "rest":
        if number + current_energy >= 100:
            gained_energy = 100 - current_energy
            current_energy = 100
        else:
            gained_energy = number
            current_energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")

    elif event_or_ingredient == "order":
        if current_energy < 30:
            current_energy += 50
            print("You had to rest!")

        else:
            current_energy -= 30
            current_coins += number
            print(f"You earned {number} coins.")

    else:
        if number > current_coins:
            print(f"Closed! Cannot afford {event_or_ingredient}.")
            flag = False
            break
        else:
            current_coins -= number
            print(f"You bought {event_or_ingredient}.")


if flag:
    print("Day completed!")
    print(f"Coins: {current_coins}")
    print(f"Energy: {current_energy}")