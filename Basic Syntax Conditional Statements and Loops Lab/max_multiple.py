divisor = int(input())
boundary = int(input())


for iteration in range(boundary, divisor - 1, -1):

    if iteration % divisor == 0:
        break

print(iteration)