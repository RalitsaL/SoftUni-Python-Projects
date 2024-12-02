n = int(input())

my_dict = {}

for n in range(n):
    info = input().split("<->")
    plant = info[0]
    rarity = int(info[1])
    rating = [0, 0]
    if info[0] not in my_dict:
        my_dict[plant] = [rarity, rating]
    else:
        my_dict[plant][0] += rarity

while True:
    command = input()
    if command == "Exhibition":
        break
    command = command.split(": ")
    action = command[0]
    the_rest_of_command = command[1]
    if action == "Rate":
        the_rest_of_command = the_rest_of_command.split(" - ")
        plant = the_rest_of_command[0]
        rating = int(the_rest_of_command[1])
        if plant not in my_dict:
            print("error")
        else:
            my_dict[plant][1][0] += rating
            my_dict[plant][1][1] += 1
    elif action == "Update":
        the_rest_of_command = the_rest_of_command.split(" - ")
        plant = the_rest_of_command[0]
        new_rarity = int(the_rest_of_command[1])
        if plant not in my_dict:
            print("error")
        else:
            my_dict[plant][0] = new_rarity
    elif action == "Reset":
        the_rest_of_command = the_rest_of_command.split(" - ")
        plant = the_rest_of_command[0]
        if plant not in my_dict:
            print("error")
        else:
            my_dict[plant][1] = [0, 0]


print("Plants for the exhibition:")
for element in my_dict:
    if my_dict[element][1][1] == 0:
        average = my_dict[element][1][0]
    else:
        average = my_dict[element][1][0] / my_dict[element][1][1]

    print(f"- {element}; Rarity: {my_dict[element][0]}; Rating: {average:.2f}")