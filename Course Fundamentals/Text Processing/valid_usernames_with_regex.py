import re
usernames = input().split(", ")
valid_usernames = []

for username in usernames:

    pattern = r'^[A-Za-z0-9]+([-_][A-Za-z0-9]+)*$'

    if bool(re.match(pattern, username)) and 3 <= len(username) <=16:
        valid_usernames.append(username)

for element in valid_usernames:
    print(element)

