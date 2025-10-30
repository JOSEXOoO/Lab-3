# Ejercicio 1 - yield
# Generar los primeros 10 números pares usando yield y recorrerlos con un for

def numeros_pares():
    for i in range(2, 21, 2):
        yield i

for num in numeros_pares():
    print(num)
