
'''
Se le pasa los argumentos a una función por medio de un diccionario.
No importa el orden como se definan los elementos.
'''

def print_info(name, lastname, age):
    print(f"Name: {name}\nLastname: {lastname}\nAge: {age}")

# Las claves deben corresponder al nombre de los parametros de la función
estudiante = {
    "name": "Juan",
    "age": 38,
    "lastname": "Cardona"
}

print_info(**estudiante)
