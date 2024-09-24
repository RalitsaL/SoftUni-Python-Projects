budget = float(input())
season = str(input())
place = ""
destination = ""
if season == "winter" or budget > 1000:
    place = "Hotel"
else:
    place = "Camp"

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        budget -= (budget * 0.70)
    elif season == "winter":
        budget -= (budget * 0.30)
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        budget -= (budget * 0.60)
    elif season == "winter":
        budget -= (budget * 0.20)
elif budget > 1000:
    destination = "Europe"
    budget -= (budget * 0.1)

print(f"Somewhere in {destination}")
print(f"{place} - {budget:.2f}")
