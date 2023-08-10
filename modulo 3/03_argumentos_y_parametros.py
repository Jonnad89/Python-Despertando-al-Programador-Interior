# Argumentos en funciones
"""
def saludar(nombre):
    print("Hola,", nombre, "Bienvenido a la clase.") 

nombre_usuario = "Juan"
saludar(nombre_usuario)
"""

#Parámetro con valores predeterminados

def saludar(nombre="amigo"):
    print("Hola,", nombre, "Bienvenido a la clase")

saludar("Carlos")

#Uso de *args y **kwargs

def mostrar_argumentos(*args, **kwargs):
    print("Argumentos posicionales:", args)
    print("Argumentos con nombre:", kwargs)

#Llamado a la funcion con argumentos posicionales

mostrar_argumentos(1, 2, 3, 4, 5)

# Llamada con argumentos con nombre
mostrar_argumentos(nombre="Juan", edad=25, cuidad="Madrid")

#Llamada con argumentos posicionales y con nombre 
mostrar_argumentos(10, 20, nombre="Ana", apelldio="García")

#Llamada con argumentos posicionales y con nombre usando *args y **kwargs

argumentos_posicionales =(5, 10, 15)
argumentos_con_nombre= {"nombre": "Luis", "profesion":"Ingeniero"}
mostrar_argumentos(*argumentos_posicionales, **argumentos_con_nombre)
