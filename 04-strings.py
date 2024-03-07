'''
Los strings representan cadenas de caracteres.
'''

nombre = "Sebastian"
texto = """Hola
me llamo sebatian.
Fullstack Developer y Data Scienst.
"""

print(texto)
print(nombre)

print(len(nombre)) # imprime la longitud del string
print(nombre[0]) # imprime el primer caracter del string

producto1 = "000 - Manzana"
print(producto1.removeprefix("000 - ")) # eliminando prefijo

producto2 = "Manzana - 000"
print(producto2.removesuffix(" - 000")) # eliminando sufijo

# indexing - se refiere a acceder a elementos especificos de un string, a traves de un indice
cadena = "Hola, Mundo"
print(cadena[0])
print(cadena[-1])

# Slicing - permite extraer un grupo de caracteres de un string
print(cadena[0:4]) # cadena[inicio, final). incluye el caracter inicial y del final lo ignora

print(cadena[6:]) # cuando no especifico un parametro de fin este toma el resto de la cadena

print(cadena[:4]) # cuando no especifico un parametro de inicio este toma todos los caracteres que esten antes del parametro fin.

print(cadena[:]) # crea una copia de mi cadena desde el inicio hasta el final

print(cadena[::2]) # especifico que su salto va a ser de 2 en 2

telefono = "4-5-6-5-2-4-3-2"

print(telefono[::2])