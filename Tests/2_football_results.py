result_1 = str(input())
result_2 = str(input())
result_3 = str(input())
counter_wins = counter_lost = counter_drawn = 0

if int(result_1[0]) > int(result_1[2]):
    counter_wins += 1
elif int(result_1[0]) < int(result_1[2]):
    counter_lost += 1
elif int(result_1[0]) == int(result_1[2]):
    counter_drawn += 1
if int(result_2[0]) > int(result_2[2]):
    counter_wins += 1
elif int(result_2[0]) < int(result_2[2]):
    counter_lost += 1
elif int(result_2[0]) == int(result_2[2]):
    counter_drawn += 1
if int(result_3[0]) > int(result_3[2]):
    counter_wins += 1
elif int(result_3[0]) < int(result_3[2]):
    counter_lost += 1
elif int(result_3[0]) == int(result_3[2]):
    counter_drawn += 1

print(f"Team won {counter_wins} games.")
print(f"Team lost {counter_lost} games.")
print(f"Drawn games: {counter_drawn}")