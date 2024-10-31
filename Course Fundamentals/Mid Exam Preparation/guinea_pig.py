food_qty = float(input()) * 1000
hay_qty = float(input()) * 1000
cover_qty = float(input()) * 1000
weight = float(input()) * 1000
something_is_not_enough = False

for day in range(1, 31):

    if food_qty >= 300:
        food_qty -= 300
    else:
        something_is_not_enough = True
        break

    if day % 2 == 0:
        if hay_qty >= 0.05 * food_qty:
            hay_qty -= 0.05 * food_qty
        else:
            something_is_not_enough = True
            break

    if day % 3 == 0:
        if cover_qty >= 1/3 * weight:
            cover_qty -= 1/3 * weight
        else:
            something_is_not_enough = True
            break

if something_is_not_enough:
    print("Merry must go to the pet store!")
else:
    if food_qty == 0 or hay_qty == 0 or cover_qty == 0:
        print("Merry must go to the pet store!")
    else:
        print(f"Everything is fine! Puppy is happy! Food: {(food_qty/1000):.2f}, Hay: {(hay_qty/1000):.2f}, Cover: {(cover_qty/1000):.2f}.")



