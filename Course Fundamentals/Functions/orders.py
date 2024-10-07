drink = input()
quantity = int(input())


def total_price():
    if drink == "coffee":
        return quantity * 1.5
    elif drink == "coke":
        return quantity * 1.4
    elif drink == "water":
        return quantity * 1
    elif drink == "snacks":
        return quantity * 2


print(f"{total_price():.2f}")