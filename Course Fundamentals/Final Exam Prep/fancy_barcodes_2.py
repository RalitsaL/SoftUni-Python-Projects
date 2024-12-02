import re
n = int(input())
pattern = r"\@\#{1,}([A-Z][a-zA-Z0-9]{4,}[A-Z])\@\#{1,}"
for _ in range(n):
    barcode = input()
    valid = re.match(pattern, barcode)
    if valid:
        product_group = ""
        for match in valid.group(1):
            if match.isdigit():
                product_group += match
        product_group = product_group or "00"
        print(f"Product group: {product_group}")

    else:
        print(f"Invalid barcode")