health = 100
bitcoin = 0
dungeons_rooms = input().split("|")
alive = True
for element in dungeons_rooms:
    element = element.split(" ")
    action = element[0]
    number = int(element[1])
    if action == "potion":
        if health + number >= 100:
            number = 100 - health
            health = 100
        else:
            health = health + number
        print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")
    elif action == "chest":
        bitcoin += number
        print(f"You found {number} bitcoins.")
    else:
        if number < health:
            print(f"You slayed {action}.")
            health -= number

        else:
            print(f"You died! Killed by {action}.")
            print(f'Best room: {dungeons_rooms.index(" ".join(element)) + 1}')
            alive = False
            break

if alive:
    print(f"You've made it!\nBitcoins: {bitcoin}\nHealth: {health}")