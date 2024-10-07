number = int(input())


def perfect_number(num: int) -> str:

    sum_divisors = 0
    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            sum_divisors += i

    if sum_divisors == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


print(perfect_number(number))