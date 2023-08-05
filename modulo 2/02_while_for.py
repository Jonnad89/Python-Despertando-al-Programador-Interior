"""contador = 0
while contador < 5:
    print("El contador es:", contador)
    contador +=1


frutas = ["manzana", "platano", "naranja", "pera"]
for fruta in frutas:
    print("Me gusta la", fruta)

for numero in range(1,6):
    print(numero)

# Suma de los primeros N números naturales
N = 10
suma = 0
contador = 1

while contador <= N:
    suma += contador
    contador +=1

print("La suma de los primeros", N, "números naturales es: ", suma)


# Cálculo e factorial

numero = 5
factorial = 1
contador = 1

while contador <= numero:
    factorial *= contador
    contador += 1

print("El factoria de", numero, "es: ", factorial)


# Imprimir patrón numérico

filas = 5

for i in range(1, filas+1):
    for j in range(1, i+1):
        print(j, end= " ")
    print()    
"""

# Conteo de letras en una cadena

texto = "Python es increíble"
letra_a_contar = "e"
contador = 0

for letra in texto:
    if letra == letra_a_contar:
        contador += 1

print("La letra", letra_a_contar, "aparece", contador, "veces en el texto")       