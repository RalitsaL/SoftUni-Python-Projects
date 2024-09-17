number_wins = 0
number_losses = 0
number_matches = 0

while True:
    name_tournament = input()
    if name_tournament == "End of tournaments":
        break

    number_of_games = int(input())
    for game_number in range(1, number_of_games +1):
        desi_team_points = int(input())
        other_team_points = int(input())
        number_matches += 1
        diff_between_points = abs(desi_team_points - other_team_points)

        if desi_team_points > other_team_points:
            number_wins += 1
            print(f"Game {game_number} of tournament {name_tournament}: win with {diff_between_points} points.")
        else:
            number_losses += 1
            print(f"Game {game_number} of tournament {name_tournament}: lost with {diff_between_points} points.")

wins_percent = (number_wins / number_matches) * 100
losses_percent = (number_losses / number_matches) * 100

print(f"{wins_percent:.2f}% matches win")
print(f"{losses_percent:.2f}% matches lost")