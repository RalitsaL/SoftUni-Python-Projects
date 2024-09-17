from math import floor
number_tournirs = int(input())
starting_points = int(input())
points_earn = 0
counter_wins = 0
for _ in range(number_tournirs):
    etap = input()

    if etap == "W":
        points_earn += 2000
        counter_wins += 1
    if etap == "F":
        points_earn += 1200
    if etap == "SF":
        points_earn += 720

average_points = points_earn / number_tournirs

print(f"Final points: {starting_points + points_earn}")
print(f"Average points: {floor(average_points)}")
print(f"{((counter_wins / number_tournirs) * 100):.2f}%")