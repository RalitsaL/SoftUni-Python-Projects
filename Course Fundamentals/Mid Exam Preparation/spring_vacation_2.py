def trip_calculator():

    days = int(input())
    budget = float(input())
    num_ppl = int(input())
    fuel_cost_per_km = float(input())
    food_expense_per_person_per_day = float(input())
    hotel_price_per_person_per_night = float(input())

    total_food_expense = food_expense_per_person_per_day * num_ppl * days

    if num_ppl > 10:
        total_hotel_expense = hotel_price_per_person_per_night * num_ppl * days * 0.75
    else:
        total_hotel_expense = hotel_price_per_person_per_night * num_ppl * days

    total_expenses = total_food_expense + total_hotel_expense

    for day in range(1, days + 1):
        distance_per_day = float(input())

        daily_fuel_expense = distance_per_day * fuel_cost_per_km
        total_expenses += daily_fuel_expense

        if day % 3 == 0 or day % 5 == 0:
            total_expenses += total_expenses * 0.4

        if day % 7 == 0:
            total_expenses -= total_expenses / num_ppl

        if total_expenses > budget:
            print(f"Not enough money to continue the trip. You need {total_expenses - budget:.2f}$ more.")
            return

    remaining_budget = budget - total_expenses
    print(f"You have reached the destination. You have {remaining_budget:.2f}$ budget left.")

trip_calculator()