'''
Nos permite omitir el resto del flujo dentro de un bucle, que esta debajo de la sentencia continue.
'''
nums = [34,10,23,57,19,2,8,3,5,6,10,20,100,80,23,24,6,77,70,125,290]

for n in nums:
  if n%2 != 0:
    continue # Cuando el número no es par. Se omite las sentencias que se encuentren abajo.
  print(n, end=", ")