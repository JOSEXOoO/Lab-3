# Ejercicio 2 - filter()
# Filtrar las palabras que empiezan con “p” de la lista ["perro","gato","pato","hamster"]

animales = ["perro", "gato", "pato", "hamster"]
con_p = list(filter(lambda x: x.lower().startswith("p"), animales))
print(con_p)
