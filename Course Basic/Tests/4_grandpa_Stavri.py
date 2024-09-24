number_days = int(input())
counter_quantity = 0
counter_degrees = 0

for _ in range(1, number_days + 1):
    quantity = float(input())
    degrees = float(input())

    counter_quantity += quantity
    counter_degrees += quantity * degrees

degrees_total = counter_degrees / counter_quantity

print(f"Liter: {counter_quantity:.2f}")
print(f"Degrees: {degrees_total:.2f}")

if degrees_total < 38:
    print(f"Not good, you should baking!")
elif 38 <= degrees_total <= 42:
    print(f"Super!")
else:
    print(f"Dilution with distilled water!")