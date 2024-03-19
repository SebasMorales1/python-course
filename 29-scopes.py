'''
El scope es el alcanze que tienen las variables para ser usadas.

Las variables con un scope global son aquellas que no estan definidas dentro de una función.

Las variables locales son las que estan dentro del cuerpo de una función y no pueden ser
accedidas por un scope global. 
'''

nombre = "Sebastian"

# scope global
def imprimir_nombre():
  #global nombre # Le decimos a la función que vamos a usar una variable con un scope global
  nombre = "Juan"
  print(f"Nombre: {nombre}")

imprimir_nombre()
print(nombre)

#scope local
def func():
  local = "Carlos"
  print(f"Hola {local}")

func()
#print(local) Las variables locales son solo validas dentro del scope de la función

#scope enclosing

def print_name():
  name = "Edward"
  edad = 30
  print(f"Hola {name}, como estas?")

  def print_age():
    nonlocal edad # nos permite acceder a variables locales de un scope superior

    edad = 40
    print(f"Su edad es {edad}")
  print_age()

print_name()