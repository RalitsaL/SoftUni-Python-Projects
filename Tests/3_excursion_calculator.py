number_peoples = int(input())
season = input()
price_per_person = 0
if number_peoples <= 5:
    if season == "spring":
        price_per_person = 50
    elif season == "summer":
        price_per_person = 48.5
    elif season == "autumn":
        price_per_person = 60
    elif season == "winter":
        price_per_person = 86

else:
    if season == "spring":
        price_per_person = 48
    elif season == "summer":
        price_per_person = 45
    elif season == "autumn":
        price_per_person = 49.5
    elif season == "winter":
        price_per_person = 85

total_price = number_peoples * price_per_person

if season == "summer":
    total_price -= 0.15 * total_price
elif season == "winter":
    total_price += 0.08 * total_price

print(f"{total_price:.2f} leva.")