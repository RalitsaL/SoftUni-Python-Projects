def multiplication_sign(a, b, c):

    list_numbers = [a, b, c]
    if a > 0 and b > 0 and c > 0:
        return "positive"
    elif a == 0 or b == 0 or c == 0:
        return "zero"
    else:
        neg_count = len(list(filter(lambda x: (x < 0), list_numbers)))
        if neg_count == 1 or neg_count == 3:
            return "negative"
        else:
            return "positive"


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(multiplication_sign(num1, num2, num3))

