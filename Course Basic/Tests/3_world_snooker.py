etap = str(input())
ticket_type = str(input())
number_tickets = int(input())
picture = str(input())

ticket_price = 0
price_picture = 0


if etap == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = 55.50
    elif ticket_type == "Premium":
        ticket_price = 105.20
    elif ticket_type == "VIP":
        ticket_price = 118.90

elif etap == "Semi final":
    if ticket_type == "Standard":
        ticket_price = 75.88
    elif ticket_type == "Premium":
        ticket_price = 125.22
    elif ticket_type == "VIP":
        ticket_price = 300.40

elif etap == "Final":
    if ticket_type == "Standard":
        ticket_price = 110.10
    elif ticket_type == "Premium":
        ticket_price = 160.66
    elif ticket_type == "VIP":
        ticket_price = 400

total_price_all_tickets = ticket_price * number_tickets
discount = 0

if 4000 >= total_price_all_tickets > 2500:
    discount = 0.10
elif total_price_all_tickets > 4000:
    discount = 0.25


if picture == "Y":
    if total_price_all_tickets > 4000:
        price_picture = 0
    else:
        price_picture = 40

total_price = total_price_all_tickets - (total_price_all_tickets * discount) + (number_tickets * price_picture)

print(f"{total_price:.2f}")