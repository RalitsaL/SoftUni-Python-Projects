period = int(input())
doctors = 7
ne_pregledani = pregledani = 0

for day in range(1, period + 1):

    patients = int(input())

    if day % 3 == 0 and ne_pregledani > pregledani:
        doctors += 1

    if patients > doctors:
        ne_pregledani += patients - doctors
        pregledani += doctors
    elif patients <= doctors:
        pregledani += patients



print(f"Treated patients: {pregledani}.")
print(f"Untreated patients: {ne_pregledani}.")
