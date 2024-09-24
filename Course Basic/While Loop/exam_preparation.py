total_tasks = 0
max_fails = max_fails_counter = int(input())
total_grade = 0
last_task = ""

while max_fails_counter > 0:
    new_task = input()

    if new_task == "Enough":
        print(f"Average score: {(total_grade / total_tasks):.2f}")
        print(f"Number of problems: {total_tasks}")
        print(f"Last problem: {last_task}")
        break

    last_task = str(new_task)
    task_score = int(input())
    total_tasks += 1
    total_grade += task_score

    if task_score <= 4:
        max_fails_counter -= 1

if max_fails_counter <= 0:
    print(f"You need a break, {max_fails} poor grades.")