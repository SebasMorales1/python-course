'''
Las tuplas son inmutables, estas representan una lista de datos que no puede ser
modificada. Cada elemento de la tupla esta separado por una ",".
'''
tupla1 = (1, False, "Juan", 0.322)
tupla2: tuple = 2, 99, True # Pueden ser definidas sin parentesis

print(tupla1)
print(type(tupla2))

def regresar_estudiante():
  return ("Juan", 18, 8.5)

# los elemetos se desenpaquetan del retorno de la función y estos son asignados a diferentes variables
nombre, edad, promedio = regresar_estudiante()

print(f"Nombre del estudiante: {nombre}")
print(f"Edad del estudiante: {edad}")
print(f"Promedio del estudiante: {promedio}")

# one-line swapping. Sirve para intercambiar valores de diferentes variables entre si con una tupla
var1 = 1.0
var2 = 2.0

var1, var2 = (var2, var1)

print(var1, var2)