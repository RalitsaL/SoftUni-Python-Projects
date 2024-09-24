yearly_tax = int(input())

sneakers_price = 0.6 * yearly_tax
drehi = 0.8 * sneakers_price
ball = 0.25 * drehi
accessories = 0.2 * ball
total = sneakers_price + drehi + ball + accessories + yearly_tax

print(f"{total:.2f}")