# Ejercicio 2 - iter()
# Crear un generador de números impares del 1 al 20 usando yield en una clase e iterarlo con un for

class Impares:
    def __iter__(self):
        for i in range(1, 21, 2):
            yield i

for n in Impares():
    print(n)
