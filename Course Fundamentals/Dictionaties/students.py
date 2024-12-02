data = input()

courses = {}

while ":" in data:
    name, id, course = data.split(":")
    if course not in courses:
        courses[course] = {id:name}
    else:
        courses[course][id] = name
    data = input()

course_name = data.replace("_", " ")
students = courses[course_name]

for id, name in students.items():
    print(f"{name} - {id}")
