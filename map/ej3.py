# Ejercicio 3 - map()
# Dada la lista ["uno","dos","tres"], crear otra lista con la longitud de cada palabra usando map()

palabras = ["uno", "dos", "tres"]
longitudes = list(map(lambda p: len(p), palabras))
print(longitudes)
