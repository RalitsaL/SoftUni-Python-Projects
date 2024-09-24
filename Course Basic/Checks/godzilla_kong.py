budget = float(input())
statists = int(input())
money_clothes_per_one_statist = float(input())
decor = 0.1 * budget
money_clothes = statists*money_clothes_per_one_statist

if statists > 150:
    money_clothes -= 0.10 * money_clothes

total_money_needed = decor + money_clothes

if total_money_needed > budget:
    print("Not enough money!")
    print(f"Wingard needs {(total_money_needed - budget):.2f} leva more.")

elif total_money_needed <= budget:
    print("Action!")
    print(f"Wingard starts filming with {(budget - total_money_needed):.2f} leva left.")
