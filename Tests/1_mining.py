from math import ceil
video_karta_cena = int(input())
prehodnik_cena = int(input())
tok_den_karta = float(input())
pechalba_karta_den = float(input())

total_price_karti = video_karta_cena * 13
total_price_prehodnici = prehodnik_cena * 13
total_poharcheni = total_price_karti + total_price_prehodnici + 1000
pechalba_den_karta = pechalba_karta_den - tok_den_karta
total_pechalba_karta_den = 13 * pechalba_den_karta

days = ceil(total_poharcheni / total_pechalba_karta_den)

print(total_poharcheni)
print(days)