lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
counter_shields_breaks = 0
for index in range(1, lost_fights_count + 1):
    if index % 2 == 0:
        expenses += helmet_price
    if index % 3 == 0:
        expenses += sword_price
    if index % 2 == 0 and index % 3 == 0:
        expenses += shield_price
        counter_shields_breaks += 1
    if counter_shields_breaks % 2 == 0 and counter_shields_breaks != 0:
        expenses += armor_price
        counter_shields_breaks = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")
