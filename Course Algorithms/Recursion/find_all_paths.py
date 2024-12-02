def find_all_paths(rows, columns, lab, direction, path):
    if rows < 0 or columns < 0 or rows >= len(lab) or columns >= len(lab[0]):
        return


    if lab[rows][columns] == "*":
        return
    if lab[rows][columns] == "v": # already visited
        return

    path.append(direction)

    if lab[rows][columns] == "e":
        print("".join(path))
    else:
        lab[rows][columns]  = "v"

        find_all_paths(rows -1, columns, lab, "U", path)
        find_all_paths(rows +1, columns, lab, "D", path)
        find_all_paths(rows, columns - 1, lab, "L", path)
        find_all_paths(rows, columns + 1, lab, "R", path)
        lab[rows][columns] = "-"

    path.pop()




rows = int(input())
columns = int(input())

lab = []
for _ in range(rows):
    lab.append(list(input()))

find_all_paths(0, 0, lab, "", [])