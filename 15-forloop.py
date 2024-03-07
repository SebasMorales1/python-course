'''
El forloop es un tipo de bucle que es utilizado para recorrer una secuencia de datos o un objeto iterable. Como una lista, diccionarios, tuplas, sets y strings.

Un iterable es un objeto que puede retornar sus elementos 1 a uno segun sean pedidos.

Tambien con el bucle for podemos Realizar una misma tarea un número x de veces.
'''

nombres = ["juan", "kebin", "luis"]
precios = {
  "manzana": 20,
  "mango": 10,
  "banano": 15
}

for nombre in nombres:
  print(nombre)

for precio in precios.items():
  print(f"{precio[0]}: {precio[1]}$")

alfabeto = {"a", "b", "c", "d", "e", "f"}

for letra in alfabeto:
  print(letra)