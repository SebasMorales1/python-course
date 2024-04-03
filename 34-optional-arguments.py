'''
Son argumentos que son opcionales para una función
'''

# Definimos el parametro descuento como opcional, tendra un valor por defecto de 0
def calcular_precio(nombre_producto, cantidad, precio_u, descuento=0):
    precio_final = precio_u * cantidad - (precio_u * descuento / 100)
    print(f"{nombre_producto}, precio final: {precio_final}")

calcular_precio("Camisa", 3, 30)
calcular_precio("Pantalon", 6, 30, 10)
