num_heroes = int(input())
heroes_dict = {}
for _ in range(num_heroes):
    heroes_all = input().split()
    hero_name = heroes_all[0]
    hit_points = int(heroes_all[1]) # max 100
    mana_points = int(heroes_all[2]) # max 200
    heroes_dict[hero_name] = [hit_points, mana_points]

while True:
    command = input()
    if command == 'End':
        break
    command = command.split(" - ")
    action = command[0]
    name = command[1]
    if action == "CastSpell":
        MP_needed = int(command[2])
        spell_name = command[3]
        if MP_needed <= heroes_dict[name][1]:
            heroes_dict[name][1] -= MP_needed
            print(f"{name} has successfully cast {spell_name} and now has {heroes_dict[name][1]} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        heroes_dict[name][0] -= damage
        if heroes_dict[name][0] <= 0:
            print(f"{name} has been killed by {attacker}!")
            heroes_dict.pop(name)
        else:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes_dict[name][0]} HP left!")

    elif action == "Recharge":
        amount = int(command[2])
        if heroes_dict[name][1] + amount > 200:

            amount = 200 - heroes_dict[name][1]
            heroes_dict[name][1] = 200
        else:
            heroes_dict[name][1] += amount
        print(f"{name} recharged for {amount} MP!")

    elif action == "Heal":
        amount = int(command[2])
        if heroes_dict[name][0] + amount > 100:

            amount = 100 - heroes_dict[name][0]
            heroes_dict[name][0] = 100
        else:
            heroes_dict[name][0] += amount
        print(f"{name} healed for {amount} HP!")


for hero, points in heroes_dict.items():
    print(hero)
    print(f"  HP: {points[0]}")
    print(f"  MP: {points[1]}")