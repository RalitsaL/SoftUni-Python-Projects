old_favorite = input().split(" | ")

while True:

    command = input()

    if command == "Stop!":
        break

    command = command.split(" ")

    action = command[0]

    if action == "Join":
        genre = command[1]
        if genre in old_favorite:
            pass
        else:
            old_favorite.append(genre)
    elif action == "Drop":
        genre = command[1]
        if genre in old_favorite:
            old_favorite.remove(genre)
    elif action == "Replace":
        old = command[1]
        new = command[2]
        if old in old_favorite and new not in old_favorite:
            old_favorite.insert(old_favorite.index(old), new)
            old_favorite.pop(old_favorite.index(old))

    elif action == "Prefer":
        index1 = int(command[1])
        index2 = int(command[2])
        if 0 <= index1 < len(old_favorite) and 0 <= index2 < len(old_favorite):
            old_favorite[index1], old_favorite[index2] = old_favorite[index2], old_favorite[index1]

print(" ".join(old_favorite))