from math import floor
number_tournirs = int(input())
starting_points = int(input())
total_points = starting_points
counter_wins = 0
for i in range(number_tournirs):
    etap = str(input())
    if etap == "W":
        total_points += 2000
        counter_wins += 1
    elif etap == "F":
        total_points += 1200
    elif etap == "SF":
        total_points += 720

print(f"Final points: {total_points}")
print(f"Average points: {floor((total_points - starting_points) / number_tournirs)}")
print(f"{((counter_wins / number_tournirs) * 100):.2f}%")
