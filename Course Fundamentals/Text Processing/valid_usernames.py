from string import digits, ascii_letters
usernames = input().split(", ")
allowed_chars = ascii_letters + digits + "-" + "_"

for username in usernames:

    if not 3 <= len(username) <= 16:
        continue

    contain_allowed_chars = [char in allowed_chars for char in username]

    if not all(contain_allowed_chars):
        continue

    print(username)