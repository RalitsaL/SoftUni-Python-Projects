n = int(input())
parking = {}
for i in range(n):
    command = input().split()

    if "register" in command:
        username = command[1]
        number = command[2]
        if username not in parking:
            parking[username] = number
            print(f"{username} registered {number} successfully")
        else:
            print(f"ERROR: already registered with plate number {number}")
    if "unregister" in command:
        username = command[1]
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")

for cars in parking:
    print(f"{cars} => {parking[cars]}")