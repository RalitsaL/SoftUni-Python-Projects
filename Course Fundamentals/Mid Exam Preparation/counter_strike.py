energy = int(input())
wins = 0
lose = False
while True:
    command = input()

    if command == "End of battle":
        break
    if energy == 0:
        lose = True
        break
    command = int(command)
    if command <= energy:
        wins += 1
        energy -= command
    else:
        lose = True
        break
    if wins % 3 == 0:
        energy += wins

if lose:
    print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
else:
    print(f"Won battles: {wins}. Energy left: {energy}")
