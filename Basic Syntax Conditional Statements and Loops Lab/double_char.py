while True:
    command = input()
    if command == "End":
        break
    elif command == "SoftUni":
        continue
    else:
        for letter in command:
            #letter += letter
            print(letter * 2,end="")
        print()