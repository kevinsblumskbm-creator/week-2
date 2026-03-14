try:
    vecuma_ievade = input("Ievadiet savu vecumu: ")
    vecums = int(vecuma_ievade)
    if vecums < 0 or vecums > 120:
        print("Kļūda: Ievadiet īstu vecumu.")
    