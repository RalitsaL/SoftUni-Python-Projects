targets = list(map(int, input().split()))

while True:
    command = input()

    if command == "End":
        break

    index = int(command)

    if index < len(targets):
        current_value = targets[index]
        targets[index] = -1

        for i in range(len(targets)):
            if targets[i] == -1:
                pass
            else:
                if targets[i] > current_value:
                    targets[i] -= current_value
                else:
                    targets[i] += current_value

count_targets = len([i for i in targets if i == -1])
print(f"Shot targets: {count_targets} ->"," ".join(map(str,targets)))