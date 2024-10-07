def odd_and_even(number):
    for digit in str(number):
        if int(digit) % 2 == 0:
            list_even.append(int(digit))
        else:
            list_odd.append(int(digit))
    sum_even = sum(list_even)
    sum_odd = sum(list_odd)
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"


list_even = []
list_odd = []
num = int(input())
print(odd_and_even(num))