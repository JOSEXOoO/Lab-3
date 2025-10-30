# Ejercicio 2 - map()
# Convertir la lista de grados Celsius [0, 10, 20, 30] a Fahrenheit usando map() y lambda

celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9 / 5) + 32, celsius))
print(fahrenheit)
