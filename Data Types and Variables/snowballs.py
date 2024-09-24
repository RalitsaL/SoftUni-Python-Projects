number_balls = int(input())
highest_score = best_weight = best_time = best_quality = 0

for index in range(number_balls):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    current_score = (weight / time_needed) ** quality
    if current_score > highest_score:
        highest_score = int(current_score)
        best_weight = weight
        best_time = time_needed
        best_quality = quality

print(f"{best_weight} : {best_time} = {highest_score} ({best_quality})")
