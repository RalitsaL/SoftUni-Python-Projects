countries = input().split(", ")
capitals = input().split(", ")
# info = {countries[index]:capitals[index] for index in range(len(countries))} ## second

# for index in range(len(countries)): ## first
#     print(f"{countries[index]} -> {capitals[index]}") ## first

# for country, capital in info.items(): ## second
#     print(f"{country} -> {capital}") ## second

info = dict(zip(countries, capitals))
for country, capital in info.items():
    print(f"{country} -> {capital}")