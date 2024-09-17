number_groups = int(input())
Musala = Monblan = Kilimandjaro = k2 = Everest = 0
total_people_all = 0
for group in range(number_groups):
    group = int(input())
    total_people_all +=group
    if group <= 5:
        Musala += group
    elif 5 < group <= 12:
        Monblan += group
    elif 12 < group <= 25:
        Kilimandjaro += group
    elif 25 < group <= 40:
        k2 += group
    elif group > 40:
        Everest += group

print(f"{((Musala / total_people_all) * 100):.2f}%")
print(f"{((Monblan / total_people_all) * 100):.2f}%")
print(f"{((Kilimandjaro / total_people_all) * 100):.2f}%")
print(f"{((k2 / total_people_all) * 100):.2f}%")
print(f"{((Everest / total_people_all) * 100):.2f}%")
