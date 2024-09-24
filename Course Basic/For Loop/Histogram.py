n = int(input())
sum_p1 = sum_p2 = sum_p3 = sum_p4 = sum_p5 = 0


for num in range(n):
    new_number = int(input())
    if new_number < 200:
        sum_p1 += 1
    elif 200 <= new_number < 400:
        sum_p2 += 1
    elif 400 <= new_number < 600:
        sum_p3 += 1
    elif 600 <= new_number < 800:
        sum_p4 += 1
    elif 800 <= new_number:
        sum_p5 += 1

print(f"{(sum_p1 / n * 100):.2f}%")
print(f"{(sum_p2 / n * 100):.2f}%")
print(f"{(sum_p3 / n * 100):.2f}%")
print(f"{(sum_p4 / n * 100):.2f}%")
print(f"{(sum_p5 / n * 100):.2f}%")