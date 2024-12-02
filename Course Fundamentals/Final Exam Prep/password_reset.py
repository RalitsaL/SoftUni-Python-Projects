my_string = input()

while True:
    print_ = True
    command = input()
    if command == 'Done':
        break

    command = command.split(' ')

    action = command[0]

    if action == 'TakeOdd':
        new_pass = ""
        for idx, letter in enumerate(my_string):
            if idx % 2 == 1:
                new_pass += letter
        my_string = new_pass

    elif action == 'Cut':
        index = int(command[1])
        length = int(command[2])
        substring = my_string[index:index+length]
        my_string = my_string.replace(substring, '', 1)
    elif action == 'Substitute':
        substring = command[1]
        substitute = command[2]
        if substring in my_string:
            my_string = my_string.replace(substring, substitute)
        else:
            print("Nothing to replace!")
            print_ = False

    if print_:
        print(my_string)

print(f"Your password is: {my_string}")
