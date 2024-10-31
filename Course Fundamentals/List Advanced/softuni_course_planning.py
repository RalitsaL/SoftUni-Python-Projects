def course_add(course_list, course_name_to_add):
    if not course_name_to_add in course_list:
        course_list.append(course_name_to_add)
    return course_list


def course_insert(command, course_list, course_name_to_insert):
    index = int(command[2])
    if not course_name_to_insert in course_list:
        course_list.insert(index, course_name_to_insert)
    return course_list


def course_remove(course_list, course_name):
    if course_name in course_list:
        index_to_remove = course_list.index(course_name)
        course_list.pop(index_to_remove)

    if f"{course_name}-Exercise" in course_list:
        index_to_remove = course_list.index(f"{course_name}-Exercise")
        course_list.pop(index_to_remove)
    return course_list


def course_swap(command, course_list, course_name):
    second_course = command[2]
    if (course_name in course_list) and (second_course in course_list):
        index_course_1 = course_list.index(course_name)
        index_course_2 = course_list.index(second_course)
        course_list[index_course_1], course_list[index_course_2] = course_list[index_course_2], course_list[index_course_1]

    if f"{course_name}-Exercise" in course_list:
        course_list.pop(course_list.index(f"{course_name}-Exercise"))
        course_list.insert(course_list.index(course_name) +1, f"{course_name}-Exercise")
    if f"{second_course}-Exercise" in course_list:
        course_list.pop(course_list.index(f"{second_course}-Exercise"))
        course_list.insert(course_list.index(second_course) +1, f"{second_course}-Exercise")
    else:
        pass
    return course_list


def exercises(course_list, course_name):

    if course_name in course_list:
        index_of_exercise = int(course_list.index(course_name)) + 1
        if f"{course_name}-Exercise" in course_list:
            pass
        else:

            course_list.insert(index_of_exercise, f"{course_name}-Exercise")
    else:
        course_list.append(course_name)
        course_list.append(f"{course_name}-Exercise")
    return course_list


initial_list = input().split(", ")

while True:
    initial_command = input()
    if initial_command == "course start":
        break

    command = initial_command.split(":")
    action = command[0]
    lesson_title = command[1]


    if action == "Add":
        course_add(initial_list, lesson_title)
    elif action == "Insert":
        course_insert(command, initial_list, lesson_title)
    elif action == "Remove":
        course_remove(initial_list, lesson_title)
    elif action == "Swap":
        course_swap(command,initial_list, lesson_title)
    elif action == "Exercise":
        exercises(initial_list, lesson_title)

for index, course in enumerate(initial_list):
    print(f"{index +1}.{course}")


