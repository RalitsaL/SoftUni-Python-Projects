number1 = int(input())
number2 = int(input())

for num in range(number1, number2 +1):
    num_to_str = str(num)
    even_sum = odd_sum = 0
    for index, digit in enumerate(num_to_str):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(num, end=" ")

