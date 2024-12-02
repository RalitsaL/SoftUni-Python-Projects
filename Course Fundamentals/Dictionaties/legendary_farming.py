key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
found = False
while not found:
    command = input().lower().split()
    for i in range(0, len(command), 2):
        if command[i + 1] == 'shards' or command[i + 1] == 'fragments' or command[i + 1] == 'motes':
            key_materials[command[i + 1]] += int(command[i])
            if key_materials[command[i + 1]] >= 250:
                break
        else:
            if command[i + 1] in junk:
                junk[command[i + 1]] += int(command[i])
            else:
                junk[command[i + 1]] = int(command[i])

    for material, quantity in key_materials.items():
        if quantity >= 250:
            if material == "shards":
                print("Shadowmourne obtained!")
                key_materials[material] -= 250
                found = True
            elif material == "fragments":
                print("Valanyr obtained!")
                key_materials[material] -= 250
                found = True
            elif material == "motes":
                print("Dragonwrath obtained!")
                key_materials[material] -= 250
                found = True

for element in key_materials:
    print(f"{element}: {key_materials[element]}")

for element in junk:
    print(f"{element}: {junk[element]}")
