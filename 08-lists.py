'''
Las listas Me permiten guardar colecciones de datos, ademas a diferencia de las
tuplas las listas son mutables y son utilizadas para guardar datos del mismo tipo.
'''

edades = [1, 22, 10, 16]
nombres = ["Edward", "Hernan", "Carlos"]
booleans = [True, False, True]

print(nombres[0]) 
nombres[0] = "Juan" # estoy modificando el primer elemento de la lista nombres
print(nombres[0])

# agregar elementos al final de la lista
edades.append(17)
edades.append(22)
edades.append(22)
print(edades)

# contar cuantas veces aparece un elemento en una lista
print(edades.count(22))
print(edades.count(10))

# extender una lista
lista_extendida = [99, 33, 9]
edades.extend(lista_extendida)
print(edades)

# Buscar un elemento. Si lo encuentra me devuelve su indice, si no da error
print(edades.index(22)) # Devuelve el indice del primer elemento que encuentra
# print(edades.index(100)) # error

# Agregar elementos en una posición especifica
edades.insert(0, 18)
print(edades)

# extraer elementos y retornarlos
print(edades.pop()) # remueve el ultimo elemento de mi lista y lo retorna
print(edades.pop(1)) # remueve el elemento con el indice 1 y lo retorna
print(edades)

# eliminar elementos de mi lista por valor
edades.remove(22)
print(edades)

# darle reversa a mi lista
edades.reverse()
print(edades)

# Limpiar una lista
edades.clear()
print(edades)

# organizar los elemetos de una lista
numeros = [5,3,12,3,4,1,3,22,9,2]
numeros.sort() # organiza la lista de menor a mayor
print(numeros)

numeros.sort(reverse=True) # organiza la lista de mayor a menor
print(numeros)

# Si los elementos son strings me los organiza de deacurdo a la convención ASCII