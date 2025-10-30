# Ejercicio 4 - map()
# Dada la lista [1,2,3,4,5], crear otra lista con el cuadrado de cada número usando map()

numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)
