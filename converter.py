KM_TO_MI = 0.621371
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172
USD_TO_EUR = 0.8423502
print("1. Km -> Mi")
print("2. Kg -> Lb")
print("3. L -> Gal")
print("4. USD -> EUR")
izvele = input("Ievadiet vienību (1-4):")
ievade = input("Ievadiet vērtību")
try:
    vertiba = float(ievade)
    if izvele == "1":
        rezultats = vertiba * KM_TO_MI
        print(f"{vertiba:.2f} Km = {rezultats:.2f} Mi")
    elif izvele == "2":
        rezultats = vertiba * KG_TO_LB
        print(f"{vertiba:.2f} Kg = {rezultats:.2f} Lb")
    elif izvele == "3":
        rezultats = vertiba * L_TO_GAL
        print(f"{vertiba:.2f} L = {rezultats:.2f} Gal")
    elif izvele == "4":
        rezultats = vertiba * USD_TO_EUR
        print(f"{vertiba:.2f} USD = {rezultats:.2f} EUR")
    else:
        print("Kļūda: Nepareiza izvēle")
except ValueError:
    print(f"Kļūda: {ievade} nav lietojams skaitlis")
    