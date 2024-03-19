'''
En python hay 4 maneras de pasarles parametros a una función, como "positional arguments", esta
forma permite pasarle los argumentos a una función en el orden que se haya establecido.
'''

def imprimir(nombre, apellido):
  print(f"Bienvenido {nombre} {apellido} al bootcamp.")

imprimir("Sebastian", "Morales")