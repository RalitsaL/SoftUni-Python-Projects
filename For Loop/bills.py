months = int(input())
counter_electricity = counter_water = counter_internet = counter_other = total = 0

for _ in range(months):
    electricity = float(input())
    counter_electricity += electricity
    counter_water += 20
    counter_internet += 15
    counter_other += (electricity + 35) + 0.2 * (electricity + 35)

total = counter_electricity + counter_water + counter_internet + counter_other

print(f"Electricity: {counter_electricity:.2f} lv")
print(f"Water: {counter_water:.2f} lv")
print(f"Internet: {counter_internet:.2f} lv")
print(f"Other: {counter_other:.2f} lv")
print(f"Average: {(total / months):.2f} lv")
