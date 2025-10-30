# Ejercicio 3 - filter()
# Filtrar los números mayores a 50 de la lista [10,60,30,80,50,100]

numeros = [10, 60, 30, 80, 50, 100]
mayores_50 = list(filter(lambda x: x > 50, numeros))
print(mayores_50)
