available_sum = 0
while True:
    data = input()
    if data == "NoMoreMoney":
        break
    curren_sum = float(data)
    if curren_sum >= 0:
        available_sum += curren_sum
        print(f"Increase: {curren_sum:.2f}")
    else:
        print("Invalid operation!")
        break

print(f"Total: {available_sum:.2f}")

