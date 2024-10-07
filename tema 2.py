import string


my_articol = """
Python este instrumentul principal pentru dezvoltarea proiectelor AI și machine learning (ML); prin urmare, este cea mai importantă tehnologie pe care programatorii AI o folosesc în munca lor.  Python este un limbaj pe care îl veți învăța cu ușurință și cu ajutorul căruia, cu puțin efort, veți putea obține rezultate foarte bune când vine vorba de programare AI și ML.
"""


jumatate = len(my_articol) // 2
prima_parte = my_articol[:jumatate]
a_doua_parte = my_articol[jumatate:]


prima_parte = prima_parte.upper()


prima_parte = prima_parte.strip()


a_doua_parte = a_doua_parte[::-1]


a_doua_parte = a_doua_parte.capitalize()


a_doua_parte = a_doua_parte.translate(str.maketrans('', '', string.punctuation))


rezultat_final = prima_parte + " " + a_doua_parte


print("Rezultatul final este:")
print(rezultat_final)
