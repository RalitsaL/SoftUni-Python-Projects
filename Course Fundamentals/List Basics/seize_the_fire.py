fire_level = input().split("#")
water_needed = int(input())
total_fire = 0
effort = 0

print("Cells:")

for i, element in enumerate(fire_level):
    element_split = element.split()

    if ((element_split[0] == "High" and 81 <= int(element_split[2]) <= 125)
        or (element_split[0] == "Medium" and 51 <= int(element_split[2]) <= 80)
        or (element_split[0] == "Low" and 1 <= int(element_split[2]) <= 50)):

        if water_needed < int(element_split[2]):
            continue
        else:
            total_fire += int(element_split[2])
            effort += 0.25 * int(element_split[2])
            print(f" - {element_split[2]}")
            water_needed -= int(element_split[2])

    else:
        continue

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")