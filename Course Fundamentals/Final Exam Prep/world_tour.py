stops = input()

while True:
    command = input()
    if command == "Travel":
        break
    command = command.split(":")
    action = command[0]

    if action == "Add Stop":
        index = int(command[1])
        string = command[2]

        if 0 <= index < len(stops):
            second_part = stops[index:]
            stops = stops[:index] + string + second_part
    elif action == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])

        if 0 <= start_index <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index + 1:]
    elif action == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
    print(stops)

print(f"Ready for world tour! Planned stops: {stops}")