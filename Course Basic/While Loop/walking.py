goal_steps = 10000
steps_total = 0
while steps_total < goal_steps:
    new_data = input()

    if new_data != "Going home":
        new_data = int(new_data)
        steps_total += new_data

    if new_data == "Going home":
        new_data = int(input())
        steps_total += new_data
        break

if steps_total < goal_steps:
    print(f"{goal_steps - steps_total} more steps to reach goal.")
else:
    print("Goal reached! Good job!")
    print(f"{steps_total - goal_steps} steps over the goal!")
