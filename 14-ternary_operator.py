'''
Me permite retornar un valor dependiendo de una condición en una sola linea.
'''

edad = int(input("Ingrese su edad: "))
message = "Used es mayor de edad" if edad >= 18 else "Usted es menor de edad"

#Resumimos esta logica en solo una linea
""" if edad >= 18:
  message = "Used es mayor de edad"
else:
  message = "Usted es menor de edad" """

print(message)