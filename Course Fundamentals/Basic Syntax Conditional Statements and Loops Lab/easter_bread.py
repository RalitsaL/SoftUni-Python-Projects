budget = float(input())
flour_per_kg = float(input())
one_pack_eggs = 0.75 * flour_per_kg
one_lt_milk = 1.25 * flour_per_kg

price_one_loaves = flour_per_kg + one_pack_eggs + (0.25 * one_lt_milk)

number_loaves = int(budget // price_one_loaves)
money_left = budget % price_one_loaves
colored_eggs_earned = number_loaves * 3
colored_eggs_lost = 0
for index in range(1, number_loaves + 1):
    if index % 3 == 0:
        colored_eggs_lost += (index - 2)

colored_eggs = colored_eggs_earned - colored_eggs_lost

print(f"You made {number_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")