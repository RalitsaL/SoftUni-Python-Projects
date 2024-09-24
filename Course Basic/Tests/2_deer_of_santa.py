from math import ceil, floor
number_days = int(input())
food_total_kg = int(input())
deer1_food_per_day = float(input())
deer2_food_per_day = float(input())
deer3_food_per_day = float(input())

total_food_needed = (deer1_food_per_day + deer2_food_per_day + deer3_food_per_day) * number_days

if total_food_needed > food_total_kg:
    print(f"{ceil(total_food_needed - food_total_kg)} more kilos of food are needed.")

else:
    print(f"{floor(food_total_kg - total_food_needed)} kilos of food left.")