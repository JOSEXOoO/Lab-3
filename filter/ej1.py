# Ejercicio 1 - filter()
# Filtrar los números pares de la lista [1,2,3,4,5,6,7,8,9,10] usando filter()

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)
