"""
Los objetos mutables son elementos los cuales pueden cambiar despues de ser creados,
en cambio los objetos inmutables no pueden cambiar despues de ser creados.

tipos de datos mutables: list, dict y sets
tipos de datos inmutables: int, float, string, bool and tuples
"""

lista_estudiantes = ["eduado", "Maria", "Pepe"]
lista_estudiantes_nuevos = lista_estudiantes

lista_estudiantes_nuevos.append("Alex")

print(lista_estudiantes_nuevos)
print(lista_estudiantes)

# Ambas variables apuntan al mismo espacio en memoria
print(id(lista_estudiantes))
print(id(lista_estudiantes_nuevos))