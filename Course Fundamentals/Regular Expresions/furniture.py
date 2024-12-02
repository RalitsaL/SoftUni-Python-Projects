import re

total_cost = 0
furniture_list = []

while True:
    command = input()
    if command == "Purchase":
        break

    pattern = r">>([^<]+)<<(\d+\.?\d*)!(\d+)"
    match = re.search(pattern, command)

    if match:
        furniture_name = match.group(1)
        price = float(match.group(2))
        quantity = int(match.group(3))

        furniture_list.append(furniture_name)
        total_cost += price * quantity

print("Bought furniture:")
for item in furniture_list:
    print(item)
print(f"Total money spend: {total_cost:.2f}")