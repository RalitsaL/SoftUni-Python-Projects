country = input()
ured = input()
total_score = 0
if country == "Russia":
    if ured == "ribbon":
        total_score = 9.100 + 9.400
    elif ured == "hoop":
        total_score = 9.300 + 9.800
    elif ured == "rope":
        total_score = 9.600 + 9.000

elif country == "Bulgaria":
    if ured == "ribbon":
        total_score = 9.600 + 9.400
    elif ured == "hoop":
        total_score = 9.550 + 9.750
    elif ured == "rope":
        total_score = 9.500 + 9.400

elif country == "Italy":
    if ured == "ribbon":
        total_score = 9.200 + 9.500
    elif ured == "hoop":
        total_score = 9.450 + 9.350
    elif ured == "rope":
        total_score = 9.700 + 9.150

print(f"The team of {country} get {total_score:.3f} on {ured}.")
print(f"{(((20 - total_score) /20 ) * 100):.2f}%")