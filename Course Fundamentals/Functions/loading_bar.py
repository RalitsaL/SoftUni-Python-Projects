number = int(input())


def loading_bar(num):
    if num == 100:
        return "100% Complete!" + '\n' + "[" + "".join(["%" for i in range(int(num/10))]) + "]"
    else:
        return f"{num}% " + "[" + "".join(["%" for i in range(int(num / 10))]) + \
               "".join(["." for i in range(int((100 - num) / 10))]) + "]" + '\n' + "Still loading..."


print(loading_bar(number))
