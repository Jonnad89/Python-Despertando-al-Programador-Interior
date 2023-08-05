"""
numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print(numero, "es un número par.")
else:
    print(numero, "es un número impar.")


numero = int(input("Ingresa un número: "))

for i in range(1,11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)


def calcular_promedio(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio

numeros = [5, 8, 12, 3, 10]
promedio_resultado = calcular_promedio(numeros)
print("el promedio de la lista es: ", promedio_resultado)
"""

import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres ) for i in range(longitud))
    return contrasena

# Ejemplo de uso de la función
longitud_contrasena = 10
contrasena_generada = generar_contrasena(longitud_contrasena)
print("Contraseña generada: ", contrasena_generada)