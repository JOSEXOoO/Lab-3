# Ejercicio 4 - yield
# Generar la serie de Fibonacci hasta el décimo elemento usando yield

def fibonacci():
    a, b = 0, 1
    for _ in range(10):
        yield a
        a, b = b, a + b

for num in fibonacci():
    print(num)
