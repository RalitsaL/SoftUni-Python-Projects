n1 = int(input())
n2 = int(input())
result = 0
operator = input()
even_or_odd = "even"

if operator == "+":
    result = n1 + n2
    if result % 2 != 0:
        even_or_odd = "odd"
    print(f"{n1} {operator} {n2} = {result} - {even_or_odd}")

elif operator == "-":
    result = n1 - n2
    if result % 2 != 0:
        even_or_odd = "odd"
    print(f"{n1} {operator} {n2} = {result} - {even_or_odd}")

elif operator == "*":
    result = n1 * n2
    if result % 2 != 0:
        even_or_odd = "odd"
    print(f"{n1} {operator} {n2} = {result} - {even_or_odd}")

elif (operator == "/" or operator == "%") and n2 == 0:
    print(f"Cannot divide {n1} by zero")

elif operator == "/":
    result = n1 / n2
    print(f"{n1} / {n2} = {result:.2f}")

elif operator == "%":
    result = n1 % n2
    print(f"{n1} % {n2} = {result}")