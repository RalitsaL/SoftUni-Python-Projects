my_dict = {}
while True:
    command = input()
    if command == 'End':
        break
    command = command.split(' -> ')
    name = command[0]
    id_ = command[1]
    if name not in my_dict:
        my_dict[name] = []

    if id_ not in my_dict[name]:
        my_dict[name].append(id_)

for element in my_dict:
    print(element)
    for el in my_dict[element]:
        print(f"-- {el}")