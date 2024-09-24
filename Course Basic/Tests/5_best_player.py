current_best_player = ""
current_best_player_goals = 0

while True:
    player_name = input()

    if player_name == "END":
        break
    number_goals = int(input())

    if number_goals > current_best_player_goals:
        current_best_player = player_name
        current_best_player_goals = number_goals

    if number_goals >= 10:
        break

print(f"{current_best_player} is the best player!")
if current_best_player_goals >= 3:
    print(f"He has scored {current_best_player_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {current_best_player_goals} goals.")