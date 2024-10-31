days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
total_plunder = 0
for days in range(1, days + 1):
    total_plunder += daily_plunder

    if days % 3 == 0:
        total_plunder += daily_plunder/2
    if days % 5 == 0:
        total_plunder -= 0.3*total_plunder

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {((total_plunder/expected_plunder)*100):.2f}% of the plunder.")