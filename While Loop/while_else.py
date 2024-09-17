number = 10
while number > 0:
    print(number)
    number -= 1

else:
    print("loop completed without a break")


number2 = 1
while number2 < 6:
    # print(number2)
    # if number2 % 2 == 0:
    #     continue  # така написано влиза в безкраен цикъл
    # number2 += 1

    number2 += 1
    if number %2 == 0:
        continue
    print(number2)
