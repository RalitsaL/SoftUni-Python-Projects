age = int(input())
washing_machine_price = float(input())
toy_price = (int(input()))
savings = 0.0
coefficient = 1

for years in range(1, age +1):
    if years % 2 != 0:
        savings += toy_price
    elif years % 2 == 0:
        savings += coefficient * 10
        savings -= 1
        coefficient += 1

if savings >= washing_machine_price:
    print(f"Yes! {(savings - washing_machine_price):.2f}")
else:
    print(f"No! {(washing_machine_price - savings):.2f}")
