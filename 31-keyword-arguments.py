'''
Me permite pasarle argumentos a una función sin importar el orden, solo especificando
el nombre del parametro y su valor. Estos tambien se pueden convinar con los positions arguments. 
'''

def print_info(name, lastname, age):
    print(f"Name: {name}\nLastname: {lastname}\nAge: {age}")

print_info(age=30, name="Edward", lastname="Perez")
print_info("Juan", age=18, lastname="Cardona")
