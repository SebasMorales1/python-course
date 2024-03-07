'''
Son Sets con la capacidad de ser inmutables. Esto tipo de sets tienen la ventaja de
que mejoran el rendimiento en memoria ya que no requiren designar espacio adcional
para realizar sus modificaciones.
'''

mi_frozenset = frozenset([2, 2, 3, 6, 6]) # Se le pasa un elemento iterable
print(mi_frozenset)

for x in mi_frozenset:
  print(x, end=", ")