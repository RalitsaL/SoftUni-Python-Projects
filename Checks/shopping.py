budget = float(input())
total_video_cards = int(input())
total_processors = int(input())
total_rams = int(input())

total_video_cards_price = total_video_cards * 250
total_processors_price = total_processors * (total_video_cards_price * 0.35)
total_rams_price = total_rams * (total_video_cards_price * 0.10)

total_price = total_video_cards_price + total_processors_price + total_rams_price

if total_video_cards > total_processors:
    total_price -= total_price * 0.15

if budget >= total_price:
    print(f"You have {(budget - total_price):.2f} leva left!")
else: print(f"Not enough money! You need {(total_price - budget):.2f} leva more!")