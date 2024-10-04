def calcular_factoria(n):
    resultado = 1
    while n > 1:
        resultado *= n 
        n -= 1
    return resultado
print(calcular_factoria(1))

print("====================================")

def calcular_factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
print(calcular_factorial(2))