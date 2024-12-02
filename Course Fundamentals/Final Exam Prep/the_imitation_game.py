encrypted_message = input()

while True:
    command = input()
    if command == 'Decode':
        break
    command = command.split('|')
    action = command[0]
    if action == 'Move':
        number_letters = int(command[1])
        encrypted_message = encrypted_message[number_letters:] + encrypted_message[:number_letters]

    elif action == 'Insert':
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    elif action == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

print(f"The decrypted message is: {encrypted_message}")
