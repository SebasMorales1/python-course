age = int(input("Ingresa tu edad: "))
height = int(input("Ingresa tu altura en centimetros: "))

if (age >= 18 and height >= 170) or (age >= 25 and height >= 165):
  print("Puedes participar")
else:
  print("No puedes participar")