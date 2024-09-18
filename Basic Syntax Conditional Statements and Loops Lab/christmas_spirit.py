quantity_decorations = int(input())
days_left = int(input())
christmas_spirit = 0
money_spend = 0


for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity_decorations += 2
    if day % 2 == 0:
        money_spend += quantity_decorations * 2
        christmas_spirit += 5
    if day % 3 == 0:
        money_spend += quantity_decorations * (5 + 3)
        christmas_spirit += 3 + 10
    if day % 5 == 0:
        money_spend += quantity_decorations * 15
        christmas_spirit += 17
    if day % 3 == 0 and day % 5 == 0:
        christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        money_spend += 5 + 3 + 15


if days_left % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {money_spend}")
print(f"Total spirit: {christmas_spirit}")

