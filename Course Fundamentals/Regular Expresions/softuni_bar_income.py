import re
command = input()
total_price = 0
while command != 'end of shift':
    customer_pattern = r"%([A-Z][a-z]+)%"
    product_pattern = r"<(\w+)>"
    count_pattern = r"\|([0-9]+)\|"
    price_pattern = r"([1-9][0-9]*\.?[0-9]*)\$"

    match_customer = re.findall(customer_pattern, command)
    match_product = re.findall(product_pattern, command)
    match_count = (re.findall(count_pattern, command))
    match_price = re.findall(price_pattern, command)


    if match_customer and match_product and match_price and match_count:
        total_price_per_order = int(match_count[0]) * float(match_price[0])
        print(f"{''.join(match_customer)}: {''.join(match_product)} - {total_price_per_order:.2f}")
        total_price += total_price_per_order
    command = input()

print(f"Total income: {total_price:.2f}")
