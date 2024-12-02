message = input()

while True:
    command = input()
    if command == 'Finalize':
        break
    command = command.split()
    action = command[0]
    if action == 'Encrypt':
        message = message[::-1]
        print(message)

    elif action == 'Decrypt':
        new_message = ""
        for letter in message:
            if letter.islower():
                letter = letter.upper()
                new_message += letter
            else:
                letter = letter.lower()
                new_message += letter
        message = new_message
        print(message)

    elif action == 'Substitute':
        old_char = command[1]
        new_char = command[2]
        if old_char in message:
            message = message.replace(old_char, new_char)
            print(message)
        else:
            print(f"Character not found.")

    elif action == 'Scramble':
        index = int(command[1])
        char = command[2]
        if index < len(message):
            message = message[:index] + char + message[index+1:]
            print(message)
        else:
            print(f"Index out of bounds.")
            
    elif action == 'Remove':
        substring = command[1]
        message = message.replace(substring, "")
        print(message)
    else:
        print(f"Invalid command detected!")