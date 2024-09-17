actor_name = str(input())
academy_points = float(input())
number_ot_people = int(input())
total_points = academy_points
enough_points = "false"
for person in range(number_ot_people):
    person = str(input())
    points_from_person = float(input())
    total_points += (len(person) * (points_from_person / 2))
    if total_points >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        enough_points = "true"
        break

if enough_points == "false":
    print(f"Sorry, {actor_name} you need {(1250.5 - total_points):.1f} more!")