"""
try:
    numero = int(input("Ingrese un número: "))
    division = 10 / numero
except ZeroDivisionError:
    print("No se puede dividir por cero.")
except ValueError:
    print("Ingrese un número válido.")
"""

try: 
    archivo = open("mi_archivo.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no se encontró.")
else: 
    print("Contenido de archivo:", contenido)
finally:
    archivo.close()