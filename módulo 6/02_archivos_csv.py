import csv

with open("datos.csv", "r") as archivo:
    lector_csv = csv.reader(archivo)
    for fila in lector_csv:
        print(fila)

datos = [
    ["Nombre", "Edad", "País"],
    ["Ana", 25, "España"],
    ["John", 30, "EE. UU."],
    ["Sara", 28, "Canadá"]
]

with open("nuevos_datos.csv", "w", newline="") as archivo:
    escritor_csv = csv.writer(archivo)
    for fila in datos:
        escritor_csv.writerow(fila)