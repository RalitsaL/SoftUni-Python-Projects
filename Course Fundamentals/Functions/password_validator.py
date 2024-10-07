initial_input = input()


def check_password(password):
    result = ""
    is_valid = True
    numbers = sum(c.isdigit() for c in password)
    letters = sum(c.isalpha() for c in password)
    others = len(password) - numbers - letters
    if not 6 <= len(password) <= 10:
        result += "Password must be between 6 and 10 characters" + '\n'
        is_valid = False
    if others > 0:
        result += "Password must consist only of letters and digits" + '\n'
        is_valid = False
    if numbers < 2:
        result += "Password must have at least 2 digits" + '\n'
        is_valid = False
    if is_valid:
        result += "Password is valid"

    return result


print(check_password(initial_input))
