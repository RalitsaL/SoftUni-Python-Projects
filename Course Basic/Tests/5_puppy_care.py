total_available_food = int(input()) * 1000

eaten_total = 0
while True:
    command = input()
    if command == "Adopted":
        break
    else:
        eaten_grams = int(command)
        eaten_total += eaten_grams

if total_available_food >= eaten_total:
    print(f"Food is enough! Leftovers: {(total_available_food - eaten_total)} grams.")
else:
    print(f"Food is not enough. You need {(eaten_total - total_available_food)} grams more.")