money_needed = float(input())
puzzle = int(input())
doll = int(input())
bear = int(input())
minion = int(input())
trunk = int(input())
total_orders = puzzle + doll + bear + minion + trunk

price_puzzle = puzzle * 2.60
price_doll = doll * 3
price_bear = bear * 4.10
price_minion = minion * 8.20
price_trunk = trunk * 2

total_price = price_trunk + price_bear + price_doll + price_puzzle + price_minion


if 0 < total_orders >=50:
    total_price -= (0.25 * total_price)

rent = (0.10 * total_price)

final = total_price - rent

if final >= money_needed:
    print(f"Yes! {(final - money_needed):.2f} lv left.")

else:
    print(f"Not enough money! {money_needed - final:.2f} lv needed.")