number_locations = int(input())

for _ in range(1, number_locations + 1):
    ochakvan_dobiv = float(input())
    number_days_on_location = int(input())
    total_dobiv = 0
    for _ in range(1, number_days_on_location + 1):
        dobito_zlato_per_day = float(input())
        total_dobiv += dobito_zlato_per_day

    if total_dobiv / number_days_on_location >= ochakvan_dobiv:
        print(f"Good job! Average gold per day: {(total_dobiv / number_days_on_location):.2f}.")
    else:
        print(f"You need {(ochakvan_dobiv - (total_dobiv / number_days_on_location)):.2f} gold.")