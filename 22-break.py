import random
import time
import os

META = 30
caracol1 = 0
caracol2 = 0

while True:
  """ print("Caracol #1: " + ("-"*caracol1) + "()|" + "-"*(META-caracol1) + "|°°")
  print("Caracol #2: " + ("-"*caracol2) + "()|" + "-"*(META-caracol2) + "|°°") """

  print("Caracol #1: 🏁" + " "*(META-caracol1) + "🐌")
  print("Caracol #1: 🏁" + " "*(META-caracol2) + "🐌")

  caracol1 += random.randint(1, 3)
  caracol2 += random.randint(1, 3)

  time.sleep(0.5)
  os.system("clear")

  if caracol1 >= META and caracol2 >= META:
    break

if caracol1 > caracol2:
  print("Caracol #1: 🐌")
  print("Caracol #2: 🏁" + " "*(META-caracol2) + "🐌")

  print("El caracol 1 gana")
elif caracol1 < caracol2:
  print("Caracol #1: 🏁" + " "*(META-caracol1) + "🐌")
  print("Caracol #2: 🐌")

  print("El caracol 2 gana")
else:
  print("Caracol #1: 🐌")
  print("Caracol #2: 🐌")

  print("Empate")