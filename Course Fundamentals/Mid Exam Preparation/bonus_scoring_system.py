from math import ceil
number_students = int(input())
number_lectures = int(input())
bonus = int(input())
total_bonus = 0
max_attendance = 0
for i in range(number_students):
    attendance = int(input())

    if attendance > max_attendance:
        max_attendance = attendance

if number_lectures > 0:
    total_bonus = max_attendance / number_lectures * (5 + bonus)

print(f"Max Bonus: {ceil(total_bonus)}.")
print(f"The student has attended {ceil(max_attendance)} lectures.")