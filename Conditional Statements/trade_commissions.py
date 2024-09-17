city = str(input())
deals = float(input())
commission = 0

if city == "Sofia":
    if 0 <= deals <= 500:
        commission = 0.05 * deals
    elif 500 < deals <= 1000:
        commission = 0.07 * deals
    elif 1000 < deals <= 10000:
        commission = 0.08 * deals
    elif deals > 10000:
        commission = 0.12 * deals

if city == "Varna":
    if 0 <= deals <= 500:
        commission = 0.045 * deals
    elif 500 < deals <= 1000:
        commission = 0.075 * deals
    elif 1000 < deals <= 10000:
        commission = 0.1 * deals
    elif deals > 10000:
        commission = 0.13 * deals

if city == "Plovdiv":
    if 0 <= deals <= 500:
        commission = 0.055 * deals
    elif 500 < deals <= 1000:
        commission = 0.08 * deals
    elif 1000 < deals <= 10000:
        commission = 0.12 * deals
    elif deals > 10000:
        commission = 0.145 * deals

if (city != "Sofia" and city != "Varna" and city != "Plovdiv") or deals < 0:
    print("error")
else:
    print(f"{commission:.2f}")
