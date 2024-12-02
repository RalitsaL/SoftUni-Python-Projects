command = input()
phonebook = {}
while "-" in command:
    command = command.split("-")
    name = command[0]
    number = command[1]
    phonebook[name] = number
    command = input()

for i in range(int(command)):
    command = input()
    if command not in phonebook:
        print(f"Contact {command} does not exist.")
    else:
        print(f"{command} -> {phonebook[command]}")