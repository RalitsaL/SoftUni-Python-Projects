n = int(input())
my_dict = {}
for i in range(n):
    piece = input().split("|")
    my_dict[piece[0]] = [piece[1], piece[2]]

command = input()
while command != "Stop":
    command = command.split("|")
    action = command[0]

    if action == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]

        if piece in my_dict:
            print(f"{piece} is already in the collection!")
        else:
            my_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == "Remove":
        piece = command[1]
        if piece in my_dict:
            my_dict.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == "ChangeKey":
        piece = command[1]
        new_key = command[2]
        if piece in my_dict:
            my_dict[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")


    command = input()

for key, value in my_dict.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")