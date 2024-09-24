people_in_jury = int(input())
number_of_presentations = 0
total_score = 0
while True:
    presentation_name = input()
    if presentation_name == "Finish":
        break

    number_of_presentations += 1
    score_per_presentation = 0.0

    for grade_per_person in range(1, people_in_jury + 1):
        grade = float(input())
        score_per_presentation += grade

    average_score_per_presentation = score_per_presentation / people_in_jury
    total_score += average_score_per_presentation
    print(f"{presentation_name} - {average_score_per_presentation:.2f}.")

print(f"Student's final assessment is {(total_score / number_of_presentations):.2f}.")