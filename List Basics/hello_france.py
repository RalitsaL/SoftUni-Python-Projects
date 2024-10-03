collection = input().split("|")
budget = float(input())
total_spend = 0
item_price = 0
for i, elements in enumerate(collection):
    items = elements.split("->")
    item_price = float(items[1])
    item_type = items[0]
    if ((item_type == "Clothes" and item_price <= 50)
        or (item_type == "Shoes" and item_price <= 35)
        or (item_type == "Accessories" and item_price <= 20.50)):

        if item_price > budget:
            continue
        else:
            budget -= item_price
            total_spend += item_price
            item_price_after = 1.4 * item_price
            print(f"{item_price_after:.2f}", end=" ")
    else:
        continue

    profit = total_spend * 0.4

print(f"\nProfit: {profit:.2f}")

money_available = (total_spend * 1.4) + budget
if money_available >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")



