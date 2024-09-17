type_film = str(input())
rows = int(input())
columns = int(input())

number_of_seats = rows * columns
total_price = 0

if type_film == "Premiere":
    total_price = number_of_seats * 12
elif type_film == "Normal":
    total_price = number_of_seats * 7.5
elif type_film == "Discount":
    total_price = number_of_seats * 5

print(f"{total_price:.2f} leva")
