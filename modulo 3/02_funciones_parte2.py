# Conversión de grados Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) +32
    return fahrenheit

grados_celsius = 30
grados_fahrenheit = celsius_a_fahrenheit(grados_celsius)
print(grados_celsius, "grados Celsius son equivalentes a", grados_fahrenheit, "grados Fahrenheit")

# Cálculo del factorial de un número

def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

num = 5
factorial_resultado = calcular_factorial(num)
print("El factorial de", num, "es:", factorial_resultado)

# Verificación de un palíndromo
def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]

texto = "Anita lava la tina"
if es_palindromo(texto):
    print("El texto es un palíndromo")
else:
    print("El texto no es un palíndromo")