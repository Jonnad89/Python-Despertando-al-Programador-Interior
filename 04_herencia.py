class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"
    
mi_perro = Perro("Rex")
print(mi_perro.hacer_sonido())

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"
    
class GatoEspecial(Gato):
    def hacer_sonido(self):    
        sonido_anterior = super().hacer_sonido()
        return f"{sonido_anterior} ¡Soy un gato especial!"
    
gato_especial = GatoEspecial("Luna")
print(gato_especial.hacer_sonido())

class Vehiculo:
    def __init__(self, marca, modelo):
        
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        return f"Este es un {self.marca} {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, combustible):
        super().__init__(marca, modelo)
        self.combustible = combustible

    def describir(self):
        return f"Este es un coche {self.marca} {self.modelo} que funciona con {self.combustible}"

mi_coche = Coche("Toyota", "Corolla", "gasolina")   
print(mi_coche.describir()) 