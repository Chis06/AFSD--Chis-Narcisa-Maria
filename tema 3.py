meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

print("Procesarea comenzilor:")
for student in studenti[:]:
    if comenzi:
        comanda = comenzi.pop(0)
        if comanda in meniu:
            print(f"{student} a comandat {comanda}.")
            studenti.pop(0)
            meniu.remove(comanda)
            istoric_comenzi.append(comanda)
            if tavi:
                tavi.pop()

print("\nInventar:")
for produs in set(istoric_comenzi):
    print(f"S-au comandat {istoric_comenzi.count(produs)} {produs}.")
print(f"Mai sunt {len(tavi)} tavi.")
for produs in ["ceafa", "papanasi", "guias"]:
    print(f"Mai este {produs}: {produs in meniu}.")

total_incasari = sum(preturi[produs] for produs in istoric_comenzi)
produse_ieftine = [produs for produs, pret in preturi.items() if pret <= 7]

print("\nFinanțe:")
print(f"Cantina a încasat: {total_incasari} lei.")
print("Produse care costă cel mult 7 lei:", produse_ieftine)