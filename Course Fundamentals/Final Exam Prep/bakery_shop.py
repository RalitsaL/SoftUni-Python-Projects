my_dict = {}
all_sold = 0
while True:
    command = input()

    if command == 'Complete':
        break

    command = command.split()
    action = command[0]
    quantity = int(command[1])
    food = command[2]

    if action == 'Receive':
        if quantity > 0:
            my_dict[food] = my_dict.get(food, 0) + quantity #ако го има добавя, ако не го създава с 0 и добавя

    elif action == 'Sell':
        if food not in my_dict.keys():
            print(f"You do not have any {food}.")
        else:
            if my_dict[food] >= quantity:
                all_sold += quantity
                print(f"You sold {quantity} {food}.")
                my_dict[food] -= quantity
                if my_dict[food] == 0:
                    del my_dict[food]
            else:
                all_sold += my_dict[food]
                print(f"There aren't enough {food}. You sold the last {(my_dict[food])} of them.")
                del my_dict[food]


for item in my_dict.keys():
    print(f"{item}: {my_dict[item]}")

print(f"All sold: {all_sold} goods")