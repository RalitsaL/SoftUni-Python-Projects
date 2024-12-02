food_and_quantities = input().split()
dict = {}
for element in range (0, len(food_and_quantities), 2):
    key = food_and_quantities[element]
    value = int(food_and_quantities[element+1])
    dict[key] = value

print(dict)