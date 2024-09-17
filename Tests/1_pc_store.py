procesor_dolar_price = float(input())
video_carta_dolar_price = float(input())
ram_dolar_price = float(input())
number_ram = int(input())
percent_discount = float(input())

price_procesor_lv = procesor_dolar_price * 1.57
video_card_lv = video_carta_dolar_price * 1.57
ram_lv = ram_dolar_price * 1.57
total_price_all_ram = ram_lv * number_ram
price_prosecor_after_discount = price_procesor_lv - (percent_discount * price_procesor_lv)
price_video_card_after_discount = video_card_lv - (percent_discount * video_card_lv)
total = price_prosecor_after_discount + price_video_card_after_discount + total_price_all_ram

print(f"Money needed - {total:.2f} leva.")
