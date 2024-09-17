days= int(input())
type_of_venue = str(input())
feedback = str(input())
price = 0
nights = days -1

if type_of_venue == "room for one person":
    price = nights * 18
elif type_of_venue == "apartment":
    if days < 10:
        price = nights * 25 - 0.3 * (nights * 25)
    elif 10 <= days <= 15:
        price = nights * 25 - 0.35 * (nights * 25)
    elif days > 15:
        price = nights * 25 - 0.5 * (nights * 25)
elif type_of_venue =="president apartment":
    if days < 10:
        price = nights * 35 - 0.1 * (nights * 35)
    elif 10 <= days <= 15:
        price = nights * 35 - 0.15 * (nights * 35)
    elif days > 15:
        price = nights * 35 - 0.2 * (nights * 35)

if feedback == "positive":
    price += 0.25 * price
elif feedback == "negative":
    price -= 0.1 * price

print(f"{price:.2f}")