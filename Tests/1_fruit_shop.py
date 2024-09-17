qgodi_cena = float(input())
banani_quantity = float(input())
portokali_quantity = float(input())
malini_quantity = float(input())
qgodi_quantity = float(input())


malini_price = 0.5 * qgodi_cena
portokali_price = 0.6 * malini_price
banani_price = 0.2 * malini_price

total_price = (qgodi_cena * qgodi_quantity) + (malini_price * malini_quantity) + (portokali_price * portokali_quantity) + (banani_price * banani_quantity)

print(f"{total_price}:.2f")