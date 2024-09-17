type_of_flower = str(input())
number_of_flowers = int(input())
budget = int(input())

price_for_Roses = 5
price_for_Dahlias = 3.8
price_for_Tulips = 2.8
price_for_Narcissus = 3
price_for_Gladiolus = 2.5
total_price = 0
if type_of_flower == "Roses":
    if number_of_flowers > 80:
        total_price = (number_of_flowers * price_for_Roses) - 0.1 * (number_of_flowers * price_for_Roses)
    else:
        total_price = number_of_flowers * price_for_Roses

elif type_of_flower == "Dahlias":
    if number_of_flowers > 90:
        total_price = (number_of_flowers * price_for_Dahlias) - 0.15 * (number_of_flowers * price_for_Dahlias)
    else:
        total_price = number_of_flowers * price_for_Dahlias

elif type_of_flower == "Tulips":
    if number_of_flowers > 80:
        total_price = (number_of_flowers * price_for_Tulips) - 0.15 * (number_of_flowers * price_for_Tulips)
    else:
        total_price = number_of_flowers * price_for_Tulips

elif type_of_flower == "Narcissus":
    if number_of_flowers < 120:
        total_price = (number_of_flowers * price_for_Narcissus) + 0.15 * (number_of_flowers * price_for_Narcissus)
    else:
        total_price = number_of_flowers * price_for_Narcissus
elif type_of_flower == "Gladiolus":
    if number_of_flowers < 80:
        total_price = (number_of_flowers * price_for_Gladiolus) + 0.2 * (number_of_flowers * price_for_Gladiolus)
    else:
        total_price = number_of_flowers * price_for_Gladiolus

if budget >= total_price:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {(budget - total_price):.2f} leva left.")
else:
    print(f"Not enough money, you need {(total_price - budget):.2f} leva more.")