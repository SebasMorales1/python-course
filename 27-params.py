'''
Los parametros son valores de entrada que permiten modificar la salida de la función
en base a los parametros de la función
'''
def sumar(num1: int, num2: int) -> None:
  resultado = num1 + num2
  print(f"El resultado de la suma es: {resultado}")

def resta(num1: int, num2: int) -> None:
  resultado = num1 - num2
  print(f"El resultado de la resta es: {resultado}")

def multiplicar(num1: int, num2: int) -> None:
  resultado = num1 * num2
  print(f"El resultado de la multiplicación es: {resultado}")

sumar(2,3)
resta(10,5)
multiplicar(2,11)