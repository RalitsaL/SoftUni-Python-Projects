sum_prime = sum_non_prime = 0


while True:
    command = input()
    non_prime_num = False
    if command == "stop":
        break

    new_num = int(command)

    if new_num < 0:
        print(f"Number is negative.")
        continue

    if new_num <= 1:
        sum_non_prime += new_num
        non_prime_num = True

    else:
        for number in range(2, int(new_num ** 0.5) + 1):
            if new_num % number == 0:
                sum_non_prime += new_num
                non_prime_num = True
                break
    if not non_prime_num:
        sum_prime += new_num

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
