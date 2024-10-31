days = int(input())
budget = float(input())
ppl = int(input())
fuel_km = float(input())
food_per_day = float(input())
room_price = float(input())
enough = True
food_expenses = days * ppl * food_per_day

if ppl > 10:
    rooms_expenses = days * ppl * room_price * 0.75
else:
    rooms_expenses = days * ppl * room_price

expenses = food_expenses + rooms_expenses

for day in range (1, days + 1):
    km = float(input())
    daily_fuel = km * fuel_km
    expenses += daily_fuel

    additional_income = expenses/ppl

    if day % 3 == 0 or day % 5 == 0:
        expenses += expenses * 0.4

    if day % 7 == 0:
        expenses -= additional_income

    if expenses > budget:
        enough = False
        print(f"Not enough money to continue the trip. You need {(expenses - budget):.2f}$ more.")
        break

if enough:
    print(f"You have reached the destination. You have {(budget - expenses):.2f}$ budget left.")
