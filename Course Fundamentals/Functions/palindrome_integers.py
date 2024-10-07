initial_input = input().split(", ")


def palindrome(some_list):
    result = ""
    for element in some_list:
        if element == element[::-1]:
            result += "True" + '\n'
        else:
            result += "False" + '\n'

    return result


print(palindrome(initial_input))






