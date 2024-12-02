raw_key = input()

while True:
    command = input()
    if command == 'Generate':
        break
    command = command.split(">>>")
    action = command[0]
    if action == 'Contains':
        substring = command[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")
    elif action == 'Flip':
        Upper_Lower = command[1]
        start = int(command[2])
        end = int(command[3])
        if Upper_Lower == "Upper":
            substring = raw_key[start:end].upper()
            raw_key = raw_key[:start] + substring + raw_key[end:]
        else:
            substring = raw_key[start:end].lower()
            raw_key = raw_key[:start] + substring + raw_key[end:]
        print(raw_key)
    elif action == 'Slice':
        start = int(command[1])
        end = int(command[2])
        raw_key = raw_key[:start] + raw_key[end:]
        print(raw_key)

print(f"Your activation key is: {raw_key}")