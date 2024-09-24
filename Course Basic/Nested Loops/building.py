floors = int(input())
rooms_per_floor = int(input())
name = ""

for floor_num in range(floors, 0, -1):
    for room in range(rooms_per_floor):
        if floor_num == floors:
            name = f"L{floor_num}{room}"
        elif floor_num % 2 ==0:
            name = f"O{floor_num}{room}"
        elif floor_num % 2 != 0:
            name = f"A{floor_num}{room}"
        print(name, end=" ")
    print()


