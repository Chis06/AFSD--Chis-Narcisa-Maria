meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ['guias'] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
preturi_dict = {produs: pret for produs, pret in preturi}  # Transformăm `preturi` într-un dicționar
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]
tavi = ["tava"] * 7
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

inventar_comenzi = {}
for produs in set(istoric_comenzi):
    inventar_comenzi[produs] = istoric_comenzi.count(produs)
print("\nInventar:")
for produs in inventar_comenzi:
    print(f"S-au comandat {inventar_comenzi[produs]} {produs}.")
print(f"Mai sunt {len(tavi)} tavi.")
stocuri = {}
for produs in ["ceafa", "papanasi", "guias"]:
    stocuri[produs] = produs in meniu
for produs in stocuri:
    print(f"Mai este {produs}: {stocuri[produs]}.")

total_incasari = 0
for produs in istoric_comenzi:
    total_incasari += preturi_dict[produs]

produse_ieftine = []

for produs, pret in preturi_dict.items():
    if pret <= 7:
        produse_ieftine.append(produs)

print("\nFinanțe:")
print(f"Cantina a încasat: {total_incasari} lei.")
print("Produse care costă cel mult 7 lei:", produse_ieftine)
