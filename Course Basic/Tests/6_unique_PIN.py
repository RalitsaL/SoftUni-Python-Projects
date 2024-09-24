num1_max = int(input())
num2_max = int(input())
num3_max = int(input())

for digit1 in range(1, num1_max + 1):
    for digit2 in range(1, num2_max + 1):
        for digit3 in range(1, num3_max + 1):
            if digit1 % 2 == 0 and digit3 % 2 == 0 and (digit2 == 2 or digit2 == 3 or digit2 == 5 or digit2 == 7):
                print(f"{digit1} {digit2} {digit3}")