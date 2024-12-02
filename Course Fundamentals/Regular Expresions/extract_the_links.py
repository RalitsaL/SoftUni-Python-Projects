import re

command = input()
list_emails = []
while command:

    pattern = r"www.[a-zA-Z0-9-]+(\.[a-z]+)*\.([a-z]+)"
    match = re.search(pattern, command)
    if match:
        list_emails.append(match.group())
    command = input()

for email in list_emails:
    print(email)