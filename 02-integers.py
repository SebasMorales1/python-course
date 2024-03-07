'''
Los enteros en python representan valores númericos sin punto decimal.

En python los enteros no tienen un limite a diferencia de otros lenguajes. El limite
esta determinado por la computadora donde se ejecute el programa
'''

sueldo: int = 1000000
prestaciones: int = 3000

print("Sueldo total:", sueldo + prestaciones)

# Operaciones aritmeticas
x = 10
y = 5

print(x+y) # suma
print(x-y) # resta
print(x*y) # multiplicación
print(x/y) # división
print(x//y) # división entera (sin decimales) redondea a piso
print(x%y) # Modulo (regresa el resto de una división)
print(x**y) # Potencia

# si usamos la división entera con un número negativo este redondeara el número
# apuntando a - infinito

print(-5//2) # -3
print(-5//4) # -2