employee_happiness = list(map(int, input().split()))
factor = int(input())
employee_happiness_after_factor = [i * factor for i in employee_happiness]

average_happiness = sum(employee_happiness_after_factor) / len(employee_happiness)
count_happy_peoples = len([i for i in employee_happiness_after_factor if i >= average_happiness])
count_all_peoples = len(employee_happiness_after_factor)
happiness = count_happy_peoples / count_all_peoples
if happiness >= 0.5:
    print(f"Score: {count_happy_peoples}/{count_all_peoples}. Employees are happy!")
else:
    print(f"Score: {count_happy_peoples}/{count_all_peoples}. Employees are not happy!")