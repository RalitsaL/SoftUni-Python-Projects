v = int(input())
p1 = int(input())
p2 = int(input())
H = float(input())

total_water = H * (p1 + p2)

if total_water <= v:
    print(f"The pool is {(total_water / v) * 100:.2f}% full. Pipe 1: {((H * p1) / total_water) * 100:.2f}%. Pipe 2: {((H * p2) / total_water) * 100:.2f}%.")
else:
    print(f"For {H} hours the pool overflows with {total_water - v} liters")
