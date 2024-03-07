'''
Los Sets son una estructura de datos mutables, sus datos no estan ordenados. Ademas los objetos que estan dentro de los Sets tienen que ser Hasheables. Los Sets no permiten datos duplicados. Es utilizada comunmente para detectar si un objeto pertenece a un conjunto de elementos, esto tambien se puede hacer con las listas, pero los sets
estan optimizados para esa operación.

Los elementos hasheables quieren decir que los objetos van a tener un valor unico hasta
el final.

Los hash son valores númericos que se le asignan al valor de un objeto que es
inmutable. Los hash estan relacionados al espacio en memoria del objeto.
'''

# Declaración
# mi_set = {1, 2, 3, 5, 4} declarando un Set con elementos ya asignados
mi_set = set() # Declarando un set vacio

# Agregando elementos a un set
mi_set.add(1)
mi_set.add(2)
mi_set.add(3)
mi_set.add(4)
mi_set.add(5)

mi_set.add(2)

print(mi_set)

frutas = {"manzana", "banano", "pera", "uva"}

print("uva" in frutas) # complejidad de busqueda O(1)

# editar un elemento
frutas.remove("manzana")
frutas.add("mango")
print(frutas)

mi_set.remove(2)
mi_set.add(0)
print(mi_set)

# Eliminar y retornar el ultimo elemento
print(frutas.pop())
print(frutas) # elimina el ultimo elemento en la hash table, no el ultimo en posición

# Eliminar un elemento especifico
# Puede llegar a dar un error porque ese elemento pudo ser eliminado por el pop de arriba
frutas.remove("banano")
print(frutas)