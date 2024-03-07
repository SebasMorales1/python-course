'''
Se utiliza el ciclo while siempre que no sea seguro el número de iteraciones.

Para estructuras finitas se utliza el ciclo for.

Ciclo for: se repite N cantidad de veces
Ciclo while: se repite N cantidad de veces dependiendo de una condición.
'''
from time import sleep

nombre = ""
correo = ""
mensaje = ""

while True:
  nombre = input("Ingresa un nombre: ")
  correo = input("Ingresa un correo: ")
  mensaje = input("Ingresa un mensaje: ")

  print(f"""
    Mensaje enviado a: {nombre}

    destinatario: {correo}

    mensaje a enviar: {mensaje}
  """)

  print("Enviando correo...")
  sleep(1)
  print("Correo enviado con exito!")

  if input("ENTER para continuar o exit para salir: ") == "exit":
    print("Gracias por usar nuestro servicio")
    break