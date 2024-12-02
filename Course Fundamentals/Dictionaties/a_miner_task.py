
my_dict = {}
while True:

    command = input()
    if command == "stop":
        break

    quantity = int(input())

    if command in my_dict:
        my_dict[command] += quantity
    else:
        my_dict[command] = quantity

for key, value in my_dict.items():
    print(f"{key} -> {value}")

