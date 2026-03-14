import random
while True:
    random_skaitlis = random.randint(1, 100)
    meginajumi = 0
    max_meginajumi = 10
    uzminets = False
    while meginajumi < max_meginajumi:
        ievade = input(f"Mēģinājums {meginajumi + 1}/{max_meginajumi}. Minējums: ")
        try:
            minejums = int(ievade)
        except ValueError:
            print("Ievadiet veselu skaitli")
            continue
        meginajumi += 1
        if minejums < random_skaitlis:
            print("Par mazu")
        elif minejums > random_skaitlis:
            print("Par lielu")
        else:
            uzminets = True
            break
    if uzminets:
        print(f"Tu uzminēji {random_skaitlis} ar {meginajumi} mēģinājumiem")
    else:
        print(f"Mēģinājumi beigušies. Pareizais skaitlis = {random_skaitlis}.")
    rematch = input("Vai spēlēt vēlreiz? (j/n)").lower()
    if rematch != "j":
        break  
