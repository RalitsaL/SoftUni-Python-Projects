number_of_students = int(input())
total_grades = feil = good = very_good = exelent = 0
for _ in range(number_of_students):
    grade = float(input())
    total_grades += grade
    if grade < 3:
        feil += 1
    elif 3 <= grade < 4:
        good += 1
    elif 4 <= grade < 5:
        very_good += 1
    elif 5 <= grade:
        exelent += 1

print(f"Top students: {((exelent / number_of_students) * 100):.2f}%")
print(f"Between 4.00 and 4.99: {((very_good / number_of_students) * 100):.2f}%")
print(f"Between 3.00 and 3.99: {((good / number_of_students) * 100):.2f}%")
print(f"Fail: {((feil / number_of_students) * 100):.2f}%")
print(f"Average: {(total_grades / number_of_students):.2f}")