num = int(input())
counter_combinations = 0
for x1 in range(0, num + 1):
    for x2 in range(num +1):
        for x3 in range(0, num +1):
            if x1 + x2 + x3 == num:
                counter_combinations += 1
print(counter_combinations)