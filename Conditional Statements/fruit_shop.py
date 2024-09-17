fruit = str(input())
day_of_week = str(input())
quantity = float(input())
total_price = 0


if fruit == "apple":
    if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" \
            or day_of_week == "Friday":
        total_price = quantity * 1.2

    elif day_of_week == "Saturday" or day_of_week == "Sunday":
        total_price = quantity * 1.25


elif fruit == "banana":
    if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" \
            or day_of_week == "Friday":
        total_price = quantity * 2.5
    elif day_of_week == "Saturday" or day_of_week == "Sunday":
        total_price = quantity * 2.7


elif fruit == "orange":
    if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" \
            or day_of_week == "Friday":
        total_price = quantity * 0.85
    elif day_of_week == "Saturday" or day_of_week == "Sunday":
        total_price = quantity * 0.90


elif fruit == "grapefruit":
    if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" \
            or day_of_week == "Friday":
        total_price = quantity * 1.45
    elif day_of_week == "Saturday" or day_of_week == "Sunday":
        total_price = quantity * 1.60


elif fruit == "kiwi":
    if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" \
            or day_of_week == "Friday":
        total_price = quantity * 2.7
    elif day_of_week == "Saturday" or day_of_week == "Sunday":
        total_price = quantity * 3


elif fruit == "pineapple":
    if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" \
            or day_of_week == "Friday":
        total_price = quantity * 5.5
    elif day_of_week == "Saturday" or day_of_week == "Sunday":
        total_price = quantity * 5.6


elif fruit == "grapes":
    if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" \
            or day_of_week == "Friday":
        total_price = quantity * 3.85
    elif day_of_week == "Saturday" or day_of_week == "Sunday":
        total_price = quantity * 4.2


if (fruit != "banana" and fruit != "apple" and fruit != "grapefruit" and fruit != "kiwi" and fruit != "pineapple" \
        and fruit != "grapes" and fruit != "orange") or (day_of_week != "Monday" and day_of_week != "Tuesday" \
        and day_of_week != "Wednesday" and day_of_week != "Thursday" and day_of_week != "Friday" \
        and day_of_week != "Saturday" and day_of_week != "Sunday"):
    print("error")

else:
    print(f"{total_price:.2f}")
