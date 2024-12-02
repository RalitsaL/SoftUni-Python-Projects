products = {}
while True:
    command = input().split()
    if command[0] == "buy":
        break

    name = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if name in products:
        products[name]["quantity"] += quantity
        if products[name]["price"] != price:
            products[name]["price"] = price
    else:
        products[name] = {"quantity": quantity, "price": price}

for elements in products:
    total_sum = products[elements]["price"] * products[elements]["quantity"]
    print(f"{elements} -> {total_sum:.2f}")