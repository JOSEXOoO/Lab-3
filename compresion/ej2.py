# Ejercicio 2 - Listas por comprensión
# Crear una lista con los cuadrados de todos los números pares del 1 al 20

cuadrados_pares = [i ** 2 for i in range(1, 21) if i % 2 == 0]
print(cuadrados_pares)
