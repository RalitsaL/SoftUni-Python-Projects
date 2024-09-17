minutes = int(input())
seconds = int(input())
length = float(input())
seconds_100 = int(input())

kontrola_in_seconds = (minutes * 60) + seconds
namaleno_vreme = (length / 120) * 2.5
total_time_player = (( length / 100 ) * seconds_100) - namaleno_vreme


if kontrola_in_seconds >= total_time_player:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time_player:.3f}.")
else:
    print(f"No, Marin failed! He was {(total_time_player - kontrola_in_seconds):.3f} second slower.")