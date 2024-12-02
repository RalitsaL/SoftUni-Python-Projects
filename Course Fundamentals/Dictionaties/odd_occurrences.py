command = input().lower().split()
count = 0
occurrences = dict.fromkeys(command, count)


for word in command:
    occurrences[word] += 1

for element in occurrences:
    if occurrences[element] % 2 ==0:
        pass
    else:
        print(element, end=" ")