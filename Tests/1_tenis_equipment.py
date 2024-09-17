from math import ceil, floor
price_raketa = float(input())
number_raketi = int(input())
number_sneakers = int(input())

total_price_raketi = price_raketa * number_raketi
price_sneakers = 1/6 * price_raketa
total_price_sneakers = number_sneakers * price_sneakers
equipment = 0.2 * (total_price_sneakers + total_price_raketi)
total_price_all = total_price_sneakers + total_price_raketi + equipment


print(f"Price to be paid by Djokovic {floor(1/8 * (total_price_all))}")
print(f"Price to be paid by sponsors {ceil(7/8 * (total_price_all))}")