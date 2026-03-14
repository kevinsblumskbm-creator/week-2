try:
    vecuma_ievade = input("Ievadiet savu vecumu: ")
    vecums = int(vecuma_ievade)
    if vecums < 0 or vecums > 120:
        print("Kļūda: Ievadiet īstu vecumu.")
    else:
        aplieciba = input("Vai jums ir autovadītāja apliecība? (j/n): ").lower() == "j"
        veterans = input("Vai Jūs esat veterāns? (j/n)").lower() == "j"
        students = input("Vai Jūs esat students? (j/n)").lower() == "j"
        drikst_balsot = vecums >= 18
        drikst_iret_auto = vecums >= 21 and aplieciba
        seniora_atlaide = vecums >= 65 or veterans
        studenta_atlaide = (16 <= vecums <= 26) and students
        print("-----")

        print(f"Var balsot: {Jā √ if drikst_balsot else Nē X}")
        print(f"Var īrēt auto: {Jā √ if drikst_iret_auto else Nē X}")
        print(f"Senioru atlaide: {Jā √ if seniora_atlaide else Nē X}")
        print(f"Studentu atlaide: {Jā √ if studenta_atlaide else Nē X}")
        