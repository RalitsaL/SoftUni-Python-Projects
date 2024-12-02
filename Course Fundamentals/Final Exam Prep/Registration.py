
username = input()

while True:
    command = input()
    if command == 'Registration':
        break

    command = command.split(' ')
    action = command[0]
    if action == 'Letters':
        if command[1] == 'Lower':
            username = username.lower()
        elif command[1] == 'Upper':
            username = username.upper()
        print(username)
    elif action == 'Reverse':
        startIndex = int(command[1])
        endIndex = int(command[2])
        if 0 <= startIndex <= endIndex < len(username):
            sub_string = username[startIndex:endIndex+1]
            print(sub_string[::-1])
        else:
            pass
    elif action == 'Substring':
        substring = command[1]
        if substring in username:
            username = username.replace(substring, '')
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")
    elif action == 'Replace':
        char = command[1]
        if char in username:
            username = username.replace(char, '-')
            print(username)

    elif action == 'IsValid':
        char = command[1]
        if char in username:
            print(f"Valid username.")
        else:
            print(f"{char} must be contained in your username.")