# Ejercicio 4 - iter()
# Crear un iterador que recorra los elementos de una lista de cadenas
# y devuelva cada cadena en mayúsculas

palabras = ["python", "java", "ruby", "c++"]
mayusculas = iter(map(str.upper, palabras))

for _ in range(len(palabras)):
    print(next(mayusculas))
