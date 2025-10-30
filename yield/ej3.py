# Ejercicio 3 - yield
# Clase con __iter__() que genera los cuadrados del 1 al 10 usando yield

class Cuadrados:
    def __iter__(self):
        for i in range(1, 11):
            yield i ** 2

for c in Cuadrados():
    print(c)
