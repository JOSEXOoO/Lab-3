# Ejercicio 1 - map()
# Dada la lista [1,2,3,4,5], crear otra lista con cada elemento multiplicado por 10 usando map()

numeros = [1, 2, 3, 4, 5]
multiplicados = list(map(lambda x: x * 10, numeros))
print(multiplicados)
