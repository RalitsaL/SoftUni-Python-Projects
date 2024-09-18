orders = int(input())
total_price = 0

for _ in range(1, orders +1):
    price_per_capsule = float(input())
    days = int(input())
    needed_capsules_per_day = int(input())

    if (price_per_capsule < 0.01 or price_per_capsule > 100) or (days < 1 or days > 31) or (needed_capsules_per_day < 1 or needed_capsules_per_day > 2000):
        continue
    else:
        price_per_order = days * needed_capsules_per_day * price_per_capsule
        print(f"The price for the coffee is: ${price_per_order:.2f}")
        total_price += price_per_order

print(f"Total: ${total_price:.2f}")