#Creación de tuplas
coordenadas = (3, 4)
nombres = ("Alice", "Bob", "Chalie")
mezclados = (10, "Hola", 3.14)


print(coordenadas)
print(nombres)
print(mezclados)


print(type(coordenadas))
print(type(nombres))
print(type(mezclados))

#Ejemplo de acceso
x = coordenadas[0]
y = coordenadas[1]
print(x)
print(y)

# coordenadas[0] = 5 Esto generará un error

# Desempaquetado
nombre, edad = ("Alice", 25)
print(nombre)
print(edad)

# Tuplas en una Función de Retorno Múltiple
def obtener_coordenadas():
    x = 3
    y = 5
    return x, y

coordenada_x, coordenada_y = obtener_coordenadas()
print("Coodenada X:", coordenada_x)
print("Coodenada Y:", coordenada_y)

# Creando una Lista de Tuplas
personas = [("Alice",25 ), ("Bob", 30), ("Charlie", 28)]

for nombre, edad in personas:
    print(nombre, "Tiene", edad, "años")