favourite_book = input()
counter_checks = 0
while True:
    new_book = input()
    counter_checks += 1

    if favourite_book == new_book:
        print(f"You checked {counter_checks -1} books and found it.")
        break
    elif new_book == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {counter_checks - 1} books.")
        break


