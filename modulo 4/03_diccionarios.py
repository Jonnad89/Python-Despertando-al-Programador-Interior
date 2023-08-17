persona = {
    "nombre" : "Alice",
    "edad" : 25,
    "profesion": "ingeniera"
}

print(type(persona))
print(persona)

nombre = persona["nombre"]
edad = persona["edad"]

print(nombre)
print(edad)

persona["ubicacion"] = "Nueva York"
persona["edad"] = 26

print(persona)

del persona["edad"]
print(persona)