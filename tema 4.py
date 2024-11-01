import random

cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

incercari_ramase = 6
litere_incercate = []

for element in progres:
    print(element, end=" ")
while "_" in progres and incercari_ramase > 0:

    litera = input("Introdu o literă: ").lower()

    if len(litera) != 1 or not litera.isalpha():
        print("Te rog să introduci o singură literă.")
        continue
    if litera in litere_incercate:
        print("Ai încercat deja această literă. ")
        continue

    litere_incercate.append(litera)

    if litera in cuvant_de_ghicit:
        for i, caracter in enumerate(cuvant_de_ghicit):
            if caracter == litera:
                progres[i] = litera
        print("Corect!")
    else:
        incercari_ramase -= 1
        print("Greșit! Litera nu se gaseste in cuvânt.")

    print("Progresul cuvântului: " + " ".join(progres))
    print(f"Încercări rămase: {incercari_ramase}")

if "_" not in progres:
    print(f"Felicitări! Ai ghicit cuvântul: {cuvant_de_ghicit}")
else:
    print(f"Ai pierdut:((((! Cuvântul corect era: {cuvant_de_ghicit}")
