total_intervals = int(input())
total_points = 0
from_0 = from_11 = from_21 = from_31 = from_41 = invalid = 0
for _ in range(total_intervals):
    new_number = int(input())

    if new_number < 0 or new_number > 50:
        total_points = (total_points / 2)
        invalid += 1
    elif 0 <= new_number <= 9:
        total_points += 0.2 * new_number
        from_0 += 1
    elif 10 <= new_number <= 19:
        total_points += 0.3 * new_number
        from_11 += 1
    elif 20 <= new_number <= 29:
        total_points += 0.4 * new_number
        from_21 += 1
    elif 30 <= new_number <= 39:
        total_points += 50
        from_31 += 1
    elif 40 <= new_number <= 50:
        total_points += 100
        from_41 += 1

print(f"{total_points:.2f}")
print(f"From 0 to 9: {((from_0 / total_intervals) * 100):.2f}%")
print(f"From 10 to 19: {((from_11 / total_intervals) * 100):.2f}%")
print(f"From 20 to 29: {((from_21 / total_intervals) * 100):.2f}%")
print(f"From 30 to 39: {((from_31 / total_intervals) * 100):.2f}%")
print(f"From 40 to 50: {((from_41 / total_intervals) * 100):.2f}%")
print(f"Invalid numbers: {((invalid / total_intervals) * 100):.2f}%")