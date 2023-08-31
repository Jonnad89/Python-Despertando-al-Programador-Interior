try: 
    with open("nuevo_archivo.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no se encontró")


with open("nuevo_archivo.txt", "w") as archivo:
    archivo.write("Hola esto es un ejemplo de escritura en archivo. ")