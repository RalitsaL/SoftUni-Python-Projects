total_money = 0
while True:
    destination = input()

    if destination == "End":
        break

    money_needed_for_the_trip = float(input())
    while True:
        money_spend = float(input())
        total_money += money_spend
        if total_money >= money_needed_for_the_trip:
            total_money = 0
            print(f"Going to {destination}!")
            break

