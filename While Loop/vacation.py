money_needed = float(input())
money_available = float(input())

counting_spending_days = 0
days_total = 0

while money_available < money_needed:
    action = input()
    money_for_the_action = float(input())

    if action == "spend" and money_for_the_action >= money_available:
        money_available = 0
    elif action == "spend":
        counting_spending_days += 1
        money_available -= money_for_the_action
    elif action == "save":
        money_available += money_for_the_action
        counting_spending_days = 0

    days_total += 1

    if counting_spending_days >= 5:
        print(f"You can't save the money.")
        print(f"{days_total}")
        break

if money_available >= money_needed:
    print(f"You saved the money for {days_total} days.")
