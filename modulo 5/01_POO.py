class Estudiante: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

estudiante1 = Estudiante("Ana", 20)
estudiante2 = Estudiante("Juan", 22)

estudiante1.presentarse()
estudiante2.presentarse()

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        return "Guau guau"
    
class Gato(Animal):
    def sonido(self):
        return "Miau miau"

mi_perro = Perro("Fido")
mi_gato = Gato("Pelusa")

print(mi_perro.nombre, "dice:", mi_perro.sonido())
print(mi_gato.nombre, "dice:", mi_gato.sonido())