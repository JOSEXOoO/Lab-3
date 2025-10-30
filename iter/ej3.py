# Ejercicio 3 - iter()
# Clase que genera los cuadrados del 1 al 10 sin usar iter(),
# pero con un método que devuelve la lista completa

class Cuadrados:
    def __init__(self):
        self.numeros = [i ** 2 for i in range(1, 11)]

    def obtener_lista(self):
        return self.numeros

c = Cuadrados()
print(c.obtener_lista())
