zoo = {}
areas = {}

while True:
    command = input()
    if command == "EndDay":
        break

    parts = command.split(": ")
    action = parts[0]

    if action == "Add":
        animal_name, needed_food, area = parts[1].split("-")
        needed_food = int(needed_food)

        if animal_name not in zoo:
            zoo[animal_name] = {"needed_food": needed_food, "area": area}
            if area not in areas:
                areas[area] = []
            areas[area].append(animal_name)
        else:
            zoo[animal_name]["needed_food"] += needed_food

    elif action == "Feed":
        animal_name, food = parts[1].split("-")
        food = int(food)

        if animal_name in zoo:
            zoo[animal_name]["needed_food"] -= food
            if zoo[animal_name]["needed_food"] <= 0:
                print(f"{animal_name} was successfully fed")
                area = zoo[animal_name]["area"]
                areas[area].remove(animal_name)
                del zoo[animal_name]


print("Animals:")
for animal, data in zoo.items():
    print(f" {animal} -> {data['needed_food']}g")

hungry_areas = {area: len([a for a in animals if a in zoo]) for area, animals in areas.items() if len([a for a in animals if a in zoo]) > 0}

if hungry_areas:
    print("Areas with hungry animals:")
    for area, count in hungry_areas.items():
        print(f" {area}: {count}")