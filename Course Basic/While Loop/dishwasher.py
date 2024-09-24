number_bottles = int(input())

total_quantity_available = 750 * number_bottles
order_counter = needed_liquid_for_round = 0
number_dishes = number_tendjeri = 0
while True:
    command = input()
    order_counter += 1

    if command == "End":
        print(f"Detergent was enough!")
        print(f"{number_dishes} dishes and {number_tendjeri} pots were washed.")
        print(f"Leftover detergent {total_quantity_available} ml.")
        break
    else:
        command = int(command)

        if order_counter % 3 != 0:
            needed_liquid_for_round = 5 * command
            number_dishes += command
        else:
            needed_liquid_for_round = 15 * command
            number_tendjeri += command

        if needed_liquid_for_round > total_quantity_available:
            print(f"Not enough detergent, {needed_liquid_for_round - total_quantity_available} ml. more necessary!")
            break
        else:
            total_quantity_available -= needed_liquid_for_round