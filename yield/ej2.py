# Ejercicio 2 - yield
# Recibe una lista y devuelve solo los números impares usando yield

def impares(lista):
    for n in lista:
        if n % 2 != 0:
            yield n

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in impares(numeros):
    print(i)
