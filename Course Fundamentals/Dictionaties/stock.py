products_and_quantities = input().split()
products_to_search_for = input().split()

products_and_quantities_dict = {}

for index in range(0, len(products_and_quantities), 2):
    key = products_and_quantities[index]
    value = int(products_and_quantities[index + 1])
    products_and_quantities_dict[key] = value

for element in products_to_search_for:
    if element in products_and_quantities_dict:
        print(f"We have {products_and_quantities_dict[element]} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")