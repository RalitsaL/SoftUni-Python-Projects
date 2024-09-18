budget = int(input())
end = False
while True:
    item_cost = input()

    if item_cost == "End":
        end = True
        break
    else:
        item_cost = int(item_cost)

    if budget >= item_cost:
        budget -= item_cost
    else:
        print("You went in overdraft!")
        break

if end:
    print("You bought everything needed.")