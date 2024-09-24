from math import floor
width = float(input())
length = float(input())
high = float(input())
average_height = float(input())

obem = width * length * high
obem_staq = (average_height + 0.4 )* 2 * 2
possible_peoples = floor(obem / obem_staq)


if possible_peoples < 3:
    print("The spacecraft is too small.")
elif 3 <= possible_peoples <= 10:
    print(f"The spacecraft holds {possible_peoples} astronauts.")
elif 10 < possible_peoples:
    print("The spacecraft is too big.")