import sys
if len(sys.argv) < 2:
    print("Kļūda: Norādiet skaitli N.")
    sys.exit()
ievade = sys.argv[1]
try:
    n = int(ievade)
    if n < 1:
        print("Ievadiet pozitīvu skaitli")
        sys.exit()
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=", " if i < n else "\n")
        elif i % 3 == 0:
            print("Fizz", end=", " if i < n else "\n")
        elif i % 5 == 0:
            print("Buzz", end=", " if i < n else "\n")
        else:
            print(i, end=", " if i < n else "\n")
except ValueError:
    print(f"Kļūda:{ievade} nav derīgs skaitlis.")
        