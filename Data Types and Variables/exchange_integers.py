num1 = int(input())
num2 = int(input())

temp = num1
num1 = num2
num2 = temp

print(f"Before: \na = {temp} \nb = {num1} \nAfter:\na = {num1} \nb = {num2}")