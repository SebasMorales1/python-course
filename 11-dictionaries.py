'''
Los diccionarios son una estructura de datos que permite organizar la información
por medio de la secuencia clave: valor. El valor puede ser un objeto cualquiera y la
clave debe ser un objeto hasheable.

Los diccionarios son mutables
'''

# Declaración
estudiantes = {
  "Edward": [1.4, 4, 5],
  "Carla": [3, 5, 5],
  "Juan": [5, 5, 5]
}

diccionario = dict(Edward = [1.4, 4, 5], Carla=[3,5,5], Juan=[5,5,5])

print(estudiantes)
print(diccionario)
print(estudiantes["Edward"])

# Agregando elementos
precios_productos = dict() # Declarando un diccionario vacio, tambien se puede con "{}" 

precios_productos["manzana"] = 12
precios_productos["mango"] = 13

print(precios_productos)

# si la clave ya existe, su valor va a ser cambiado
precios_productos["mango"] = 20
print(precios_productos)

# Elimando un elemento
del precios_productos["mango"]

print(precios_productos)

# Vistas de diccionarios

#keys
print(estudiantes.keys())

# values
print(estudiantes.values())

# both
print(estudiantes.items())