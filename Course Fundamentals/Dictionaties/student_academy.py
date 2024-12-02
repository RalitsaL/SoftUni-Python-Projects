pairs = int(input())
students = {}
for i in range(pairs):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)

students_final = {}

for each in students:
    average = sum(students[each]) / len(students[each])
    if average >= 4.50:
        students_final[each] = average

for each in students_final:
    print(f"{each} -> {students_final[each]:.2f}")



