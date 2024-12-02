courses = {}
while True:
    command = input()
    if command == 'end':
        break
    command = command.split(" : ")
    course_name = command[0]
    student_name = command[1]

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

for course in courses:
    print(f"{course}: {len(courses[course])}")
    for student in courses[course]:
        print(f"-- {student}")
