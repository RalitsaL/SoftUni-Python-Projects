money_inhered = float(input())
desired_year = int(input())
current_age = 18
for year in range(1800, desired_year + 1):

    if year % 2 == 0:
        money_inhered -= 12000
    elif year % 2 == 1:
        money_inhered -= (12000 + 50 * current_age)
    current_age += 1

if money_inhered >= 0:
    print(f"Yes! He will live a carefree life and will have {money_inhered:.2f} dollars left.")
elif money_inhered <0:
    print(f"He will need {abs(money_inhered):.2f} dollars to survive.")
