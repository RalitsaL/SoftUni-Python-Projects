month = input()
total_nights = int(input())
price_studio = 0.0
price_apartament = 0.0

if month == "May" or month == "October":
    price_studio = 50
    price_apartament = 65
    if 7 < total_nights <= 14:
        price_studio -= 0.05 * price_studio
    elif total_nights > 14:
        price_studio -= 0.3 * price_studio

elif month == "June" or month == "September":
    price_studio = 75.2
    price_apartament = 68.7
    if total_nights > 14:
        price_studio -= 0.2 * price_studio

elif month == "July" or month == "August":
    price_studio = 76
    price_apartament = 77

total_amount_studio = total_nights * price_studio
total_amount_apartment = total_nights * price_apartament

if total_nights > 14:
    total_amount_apartment  -= total_amount_apartment * 0.1

print(f"Apartment: {total_amount_apartment:.2f} lv.")
print(f"Studio: {total_amount_studio:.2f} lv.")