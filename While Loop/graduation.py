name = input()
fail_counter = 0
class_counter = 1
total_grade = 0
while class_counter < 13:
    grade = float(input())

    if grade < 4:
        fail_counter += 1

    elif grade >= 4:
        class_counter += 1
        total_grade += grade

    if fail_counter == 2:
        print(f"{name} has been excluded at {class_counter} grade")
        break

if fail_counter < 2:
    print(f"{name} graduated. Average grade: {(total_grade/12):.2f}")