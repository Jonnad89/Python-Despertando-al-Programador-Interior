colores = {"rojo", "verde", "azul"}
numeros = set([1, 2, 3, 4, 5])

# print(type(colores))
# print(type(numeros))

conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

union = conjunto_a | conjunto_b
interseccion = conjunto_a & conjunto_b 
diferencia = conjunto_a - conjunto_b

# print(union)
# print(interseccion)
# print(diferencia)

frutas = {"manzana", "banana", "naranja"}

if "manzana" in frutas:
    print("La manzana está en el conjunto de frutas")


def encontrar_numeros_unicos(lista):
    numeros_unicos = set()

    for numero in lista:
        if numero not in numeros_unicos:
            numeros_unicos.add(numero)

    return numeros_unicos

numeros = [3, 7, 2, 5, 3, 7 , 9, 2, 8, 1]
unicos = encontrar_numeros_unicos(numeros)
print("Números únicos:", unicos)