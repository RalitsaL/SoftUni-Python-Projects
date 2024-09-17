stadion_total = int(input())
total_fens = int(input())
a_counter = b_counter = v_counter = g_counter = 0
for _ in range(total_fens):
    sector = input()

    if sector == "A":
        a_counter += 1
    elif sector == "B":
        b_counter += 1
    elif sector == "V":
        v_counter += 1
    elif sector == "G":
        g_counter += 1

print(f"{((a_counter / total_fens) * 100):.2f}%")
print(f"{((b_counter / total_fens) * 100):.2f}%")
print(f"{((v_counter / total_fens) * 100):.2f}%")
print(f"{((g_counter / total_fens) * 100):.2f}%")
print(f"{((total_fens / stadion_total) * 100):.2f}%")