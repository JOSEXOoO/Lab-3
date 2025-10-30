# Ejercicio 3 - lambda
# Pedir una lista de números por input y devolver el primer elemento

lista = list(map(int, input("Ingrese números separados por espacio: ").split()))

primer_elemento = lambda l: l[0] if l else "Lista vacía"
print("El primer elemento es:", primer_elemento(lista))
