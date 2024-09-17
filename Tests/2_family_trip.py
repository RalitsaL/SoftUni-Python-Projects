buget = float(input())
noshtuvki = int(input())
cena_noshtuvka = float(input())
procent_dopulnitelni_razhodi = int(input())

total_price = 0

if noshtuvki <= 7:
    total_price = (noshtuvki * cena_noshtuvka) + (procent_dopulnitelni_razhodi/100 * buget)
else:
    total_price = (noshtuvki * (0.95 * cena_noshtuvka)) + (procent_dopulnitelni_razhodi/100 * buget)

if total_price <= buget:
    print(f"Ivanovi will be left with {(buget - total_price):.2f} leva after vacation.")
else:
    print(f"{(total_price - buget):.2f} leva needed.")