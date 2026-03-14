Produkts1 = "Zemenes"
skaits = int(3)
cena_par_zemeni = float(0.80)
Produkts2 = "Bumbieri"
skaitsB = int(8)
cena_par_bumbieri = float(1.2)
print(f"Labdien, manā veikalā ir {Produkts1} un {Produkts2}")
print(f"Prece: {Produkts1}")
print(f"Daudzums: {skaits} gabali")
print(f"Maksa: {skaits * cena_par_zemeni} EUR")
print(f"Vērtība: {Produkts2} Tips: {type(Produkts2)}")
print(f"Vērtība: {skaitsB} Tips: {type(skaitsB)}")
print(f"Vērtība: {cena_par_bumbieri} Tips: {type(cena_par_bumbieri)}")
Produkts = ""
Iepirkumu_maisiņš = ["Bumbieri"]
print(f"Vai tukšs produkts ir patiess? {bool(Produkts)}")
print(f"Vai iepirkumu maisiņš ar produktiem ir patiess? {bool (Iepirkumu_maisiņš)}")
skaitlis40 = "40"
pārvērst_int = int(skaitlis40)
print(f"Pārveide: {skaitlis40} uz {pārvērst_int} ({type(pārvērst_int)})")
#Robežgadījums: int(četrdesmit), jo burtus nevar pārvērst uz cipariem. Izmet kļūdu ValueError.
teksts_cena = "10"
čeka_summa = int(teksts_cena)
print(f"Jūsu summa ir: {čeka_summa}")
#Robežgadījums: ja tekstā būtu eiro simbols. Izmet kļūdu ValueError.
precīza_cena = 15.99
cena_bez_centiem = int(precīza_cena)
print(f"Summa bez centiem: {cena_bez_centiem}")
