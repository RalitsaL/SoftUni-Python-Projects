points = int(input())
bonus_point = 0
additional_bonus = 0

if points <=100:
    bonus_point = 5

elif points > 100 and points <=1000:
    bonus_point = 0.2*points

elif points > 1000:
    bonus_point = 0.1*points

if points % 2 == 0:
    additional_bonus = 1

if points % 10 == 5:
    additional_bonus = 2

print(bonus_point + additional_bonus)
print(points + bonus_point + additional_bonus)