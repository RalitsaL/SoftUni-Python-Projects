import re

n = int(input())

for value in range(n):
    barcode = input()
    pattern = r'\@\#+([A-Z][A-Za-z0-9]{4,}[A-Z])\@\#+'
    is_valid = re.findall(pattern, barcode)

    if is_valid:
        barcode = ''.join(is_valid)
        product_group = ''.join([x for x in barcode if x.isdigit()])
        product_group = product_group or "00"
        print(f'Product group: {product_group}')
    else:
        print('Invalid barcode')