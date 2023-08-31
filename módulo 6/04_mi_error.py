# class MiErrorPersonalizado(Exception):
#     def __init__(self, mensaje):
#         super().__init__(mensaje)

# try:
#     edad = int(input("Ingresa tu edad: "))
#     if edad < 0:
#         raise MiErrorPersonalizado("La edad no puede ser negativa.")
# except MiErrorPersonalizado as error:
#     print(error)

class MiErrorValueError(ValueError):
    def __init__(self, valor):
        mensaje = f"Se produjo un error de valor: {valor}"
        super().__init__(mensaje)

try:
    nota = int(input("Ingresa tu nota: "))
    if nota < 0 or nota > 100:
        raise MiErrorValueError(nota)
except MiErrorValueError as error:
    print(error)