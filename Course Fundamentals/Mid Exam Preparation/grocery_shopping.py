products = input().split("|")

while True:
    command = input()
    if command == "Shop!":
        break

    command = command.split("%")
    action = command[0]

    if action == "Important":
        product = command[1]
        if product in products:
            products.remove(product)
        products.insert(0, product)

    elif action == "Add":
        product = command[1]
        if product in products:
            print("The product is already in the list.")
        else:
            products.append(product)
    elif action == "Swap":
        product1 = command[1]
        product2 = command[2]
        if product1 in products and product2 in products:
            idx_1 = products.index(product1)
            idx_2 = products.index(product2)
            products[idx_1], products[idx_2] = products[idx_2], products[idx_1]
        elif product1 not in products:
            print(f"Product {product1} missing!")
        elif product2 not in products:
            print(f"Product {product2} missing!")

    elif action == "Remove":
        product = command[1]
        if product in products:
            products.remove(product)
        else:
            print(f"Product {product} isn't in the list.")

    elif action == "Reversed":
        products = products[::-1]

for index, item in enumerate(products):
    print(f"{index + 1}. {item}")
