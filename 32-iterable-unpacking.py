'''
Se le pasa los argumentos a una función por medio de un objeto iterable (comunmente una tupla).
'''

def print_info(name, lastname, age):
    print(f"Name: {name}\nLastname: {lastname}\nAge: {age}")

estudiante = ("Carlos", "Gomez", 20)

print_info(*estudiante)
