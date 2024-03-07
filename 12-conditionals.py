'''
Los condicionales sirven para controlar el flujo de mi programa.
'''

edad = int(input("Ingresa tu edad: "))
MESSAGE = f"Tienes {edad} año/s."

if edad >= 18 and edad <= 35:
  print(f"Eres un adulto joven. {MESSAGE}")
elif edad > 35:
  print(f"Eres un adulto. {MESSAGE}")
else:
  print(f"Eres menor de edad. {MESSAGE}")