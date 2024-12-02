my_dict = {}
while True:
    command = input()
    if command == "statistics":
        break

    command = command.split(": ")
    key = command[0]
    value = int(command[1])
    if key in my_dict.keys():
        my_dict[key] += value
    else:
        my_dict[key] = value

total_products = len(my_dict.keys())
total_quantity = sum(my_dict.values())

print("Products in stock:")
for element in my_dict:
    print(f"- {element}: {my_dict[element]}")
print(f"Total Products: {total_products}\nTotal Quantity: {total_quantity}")
