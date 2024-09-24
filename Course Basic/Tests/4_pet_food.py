number_days = int(input())
total_food = float(input())
eaten_buiscuits = 0
total_dog = total_cat = 0
for day in range(1, number_days +1):
    dog_eaten = int(input())
    cat_eaten = int(input())

    total_dog += dog_eaten
    total_cat += cat_eaten

    if day % 3 == 0:
        eaten_buiscuits += 0.1 * (dog_eaten + cat_eaten)

total_food_eaten = total_cat + total_dog
total_buiscuids = round(eaten_buiscuits)

print(f"Total eaten biscuits: {total_buiscuids}gr.")
print(f"{((total_food_eaten / total_food) * 100):.2f}% of the food has been eaten.")
print(f"{((total_dog / total_food_eaten) * 100):.2f}% eaten from the dog.")
print(f"{((total_cat / total_food_eaten) * 100):.2f}% eaten from the cat.")

