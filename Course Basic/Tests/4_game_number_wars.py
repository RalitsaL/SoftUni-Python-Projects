player_1 = input()
player_2 = input()
counter_points_player1 = counter_points_player2 = 0

for _ in range(18):

    card_player_1 = input()

    if card_player_1 == "End of game":
        print(f"{player_1} has {counter_points_player1} points")
        print(f"{player_2} has {counter_points_player2} points")
        break

    card_player_2 = input()

    if card_player_2 == "End of game":
        print(f"{player_1} has {counter_points_player1} points")
        print(f"{player_2} has {counter_points_player2} points")
        break

    card_player_1 = int(card_player_1)
    card_player_2 = int(card_player_2)

    if card_player_1 > card_player_2:
        counter_points_player1 += card_player_1 - card_player_2
    elif card_player_2 > card_player_1:
        counter_points_player2 += card_player_2 - card_player_1
    elif card_player_1 == card_player_2:
        new_card_1 = int(input())
        new_card_2 = int(input())
        print("Number wars!")
        if new_card_1 > new_card_2:
            print(f"{player_1} is winner with {counter_points_player1} points")
        else:
            print(f"{player_2} is winner with {counter_points_player2} points")
        break