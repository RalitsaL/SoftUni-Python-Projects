from math import floor
poroda = input()
sex = input()
total_life_years = 0
valid_input = True
if poroda == "British Shorthair":
    if sex == "m":
        total_life_years = 13
    elif sex == "f":
        total_life_years = 14
elif poroda == "Siamese":
    if sex == "m":
        total_life_years = 15
    elif sex == "f":
        total_life_years = 16
elif poroda == "Persian":
    if sex == "m":
        total_life_years = 14
    elif sex == "f":
        total_life_years = 15
elif poroda == "Ragdoll":
    if sex == "m":
        total_life_years = 16
    elif sex == "f":
        total_life_years = 17
elif poroda == "American Shorthair":
    if sex == "m":
        total_life_years = 12
    elif sex == "f":
        total_life_years = 13
elif poroda == "Siberian":
    if sex == "m":
        total_life_years = 11
    elif sex == "f":
        total_life_years = 12
else:
    valid_input = False
    print(f"{poroda} is invalid cat!")

if valid_input:
    print(f"{floor((total_life_years * 12) / 6)} cat months")
