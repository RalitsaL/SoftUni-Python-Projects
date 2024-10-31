employer_one = int(input())
employer_two = int(input())
employer_three = int(input())
student_count = int(input())

employers_total_per_hour = employer_three + employer_two + employer_one

total_hours = 0

while student_count > 0:
    student_count -= employers_total_per_hour
    total_hours += 1
    if total_hours % 4 == 0:
        total_hours += 1
print(f"Time needed: {total_hours}h.")