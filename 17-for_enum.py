'''
La función enumerate nos regresa el indice y valor de un objeto iterable.
'''
letters = "abcdefghijkl"

# for index in range(len(letters)):
#   print(f"{index}: {letters[index]}")

# el enumerate hace lo mismo pero de una manera más optima y elegante.
for i, value in enumerate(letters):
  print(f"{i}: {value}")