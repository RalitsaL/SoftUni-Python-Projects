tovari = int(input())
bus = trunk = train = 0
price_bus = price_trunk = price_train = 0
total_weight = 0
for _ in range(tovari):
    weight = int(input())
    total_weight += weight
    if weight <= 3:
        bus += weight
        price_bus += 200 * weight
    elif 3 < weight <= 11:
        trunk += weight
        price_trunk += 175 * weight
    elif weight >= 12:
        train += weight
        price_train += 120 * weight

print(f"{(price_bus + price_trunk + price_train) / (bus + trunk + train):.2f}")
print(f"{((bus / total_weight) * 100):.2f}%")
print(f"{((trunk / total_weight) * 100):.2f}%")
print(f"{((train / total_weight) * 100):.2f}%")