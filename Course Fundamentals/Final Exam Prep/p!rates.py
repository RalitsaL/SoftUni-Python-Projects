my_dict = {}

command = input()

while command != 'Sail':
    command = command.split('||')
    city = command[0]
    population = int(command[1])
    gold = int(command[2])
    if city not in my_dict:
        my_dict[city] = {'population': population, 'gold': gold}
    else:
        my_dict[city]['population'] += population
        my_dict[city]['gold'] += gold

    command = input()

events = input()

while events != 'End':
    events = events.split('=>')
    action = events[0]
    town = events[1]

    if action == 'Plunder':
        people = int(events[2])
        gold = int(events[3])

        my_dict[town]['gold'] -= gold
        my_dict[town]['population'] -= people
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if my_dict[town]['population'] <= 0 or my_dict[town]['gold'] <= 0:
            print(f"{town} has been wiped off the map!")
            my_dict.pop(town)

    elif action == 'Prosper':
        gold = int(events[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            my_dict[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {my_dict[town]['gold']} gold.")

    events = input()

if my_dict:
    print(f"Ahoy, Captain! There are {len(my_dict)} wealthy settlements to go to:")
    for k, v in my_dict.items():
        print(f"{k} -> Population: {v['population']} citizens, Gold: {v['gold']} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")