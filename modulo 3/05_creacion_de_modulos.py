# Creación de tus propios módulos - Fin módulo 3
"""
import calculadora

resultado_suma = calculadora.suma(10, 5)
print("Suma: ", resultado_suma)

resultado_resta = calculadora.resta(25, 15)
print("Resta: ", resultado_resta)

resultado_multiplicacion = calculadora.multiplicacion(9, 5)
print("Multiplicación: ", resultado_multiplicacion)
"""

from mi_paquete.calculadora.funciones import suma, resta

resultado_suma = suma(10, 5)
print("Suma: ", resultado_suma)

resultado_resta = resta(15, 8)
print("El resultado de la resta es: ", resultado_resta)