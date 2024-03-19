def sumar(num1: int, num2: int) -> None:
  resultado = num1 + num2
  print(f"El resultado de la suma es: {resultado}")

def restar(num1: int, num2: int) -> None:
  resultado = num1 - num2
  print(f"El resultado de la resta es: {resultado}")

def multiplicar(num1: int, num2: int) -> None:
  resultado = num1 * num2
  print(f"El resultado de la multiplicación es: {resultado}")

print("Opciones:\n1) Suma 2) Resta 3) Multiplicación")
opc = int(input("Ingresa una opción: "))

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if opc == 1:
  sumar(num1, num2)
elif opc == 2:
  restar(num1, num2)
elif opc == 3:
  multiplicar(num1, num2)
else:
  print("Opción invalida.")