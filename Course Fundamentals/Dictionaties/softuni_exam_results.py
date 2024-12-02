results = {}
submissions = {}
while True:
    command = input()
    if command == 'exam finished':
        break
    command = command.split('-')

    if command[1] == "banned":
        results.pop(command[0])
    else:
        username = command[0]
        language = command[1]
        points = int(command[2])

        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1

        if username not in results:
            results[username] = points
        else:
            if points < results[username]:
                pass
            else:
                results[username] = points

print("Results:")
for student in results:
    print(f"{student} | {results[student]}")
print("Submissions:")
for submission in submissions:
    print(f"{submission} - {submissions[submission]}")