# Ejercicio 1 - lambda
# Crear una función lambda que reciba dos números y devuelva el mayor
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
mayor = lambda a, b: a if a > b else b
print(mayor(num1 , num2))
