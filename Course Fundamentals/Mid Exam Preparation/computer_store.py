total_netto_price_pc = 0
type_client = ""
while True:
    netto_command = input()

    if netto_command == "special" or netto_command == "regular":
        type_client = netto_command
        break

    netto_command = float(netto_command)

    if netto_command < 0:
        print("Invalid price!")
    else:
        total_netto_price_pc += netto_command

taxes = 0.2 * total_netto_price_pc
total_bruto = taxes + total_netto_price_pc

if type_client == "special":
        total_bruto = 0.9 * total_bruto

if total_netto_price_pc == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_netto_price_pc:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print(f"-----------")
    print(f"Total price: {total_bruto:.2f}$")

