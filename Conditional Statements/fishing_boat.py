budget = int(input())
season = str(input())
number_of_people = int(input())

total_price = 0

if season == "Spring":
    total_price = 3000
elif season == "Summer" or season == "Autumn":
    total_price = 4200
elif season == "Winter":
    total_price = 2600


if number_of_people <= 6:
        total_price -= 0.1 * total_price
elif 7 <= number_of_people <= 11:
        total_price -= 0.15 * total_price
elif number_of_people >= 12:
        total_price -= 0.25 * total_price

if number_of_people % 2 == 0 and season != "Autumn":
    total_price -= 0.05 * total_price

if budget >= total_price:
    print(f"Yes! You have {(budget - total_price):.2f} leva left.")
else:
    print(f"Not enough money! You need {(total_price - budget):.2f} leva.")