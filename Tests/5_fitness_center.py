people_total = int(input())
counter_Back = counter_Chest = counter_Legs = counter_Abs = counter_Protein_shake = counter_protein_bar = 0
counter_eaters = counter_training = 0
for _ in range(people_total):
    purpose = input()

    if purpose == "Back":
        counter_Back += 1
        counter_training += 1
    elif purpose == "Chest":
        counter_Chest += 1
        counter_training += 1
    elif purpose == "Legs":
        counter_Legs += 1
        counter_training += 1
    elif purpose == "Abs":
        counter_Abs += 1
        counter_training += 1
    elif purpose == "Protein shake":
        counter_Protein_shake += 1
        counter_eaters += 1
    elif purpose == "Protein bar":
        counter_protein_bar += 1
        counter_eaters += 1

print(f"{counter_Back} - back")
print(f"{counter_Chest} - chest")
print(f"{counter_Legs} - legs")
print(f"{counter_Abs} - abs")
print(f"{counter_Protein_shake} - protein shake")
print(f"{counter_protein_bar} - protein bar")
print(f"{((counter_training / people_total) * 100):.2f}% - work out")
print(f"{((counter_eaters / people_total) * 100):.2f}% - protein")


