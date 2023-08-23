"""
Atributos de Clase y de instancia:
EN POO, podemos tener atributos que son compartidos por todas las instancias de una clase(atributos de clase) y atributos únicos para cada instancia(atributos de instancia)
"""

class Coche:
    cantidad_ruedas = 4 # Atributo de clase

    def __init__(self, marca, modelo):
        self.marca = marca #Atributo de instancia
        self.modelo = modelo #Atributo de instancia

    @classmethod
    def cambiar_ruedas(cls, cantidad):
        cls.cantidad_ruedas = cantidad

    def presentarse(self):
        return f"Soy un {self.marca} {self.modelo} con {self.cantidad_ruedas} ruedas"  

# Creación de objetos:
coche1 = Coche("Toyota", "Corolla")  
coche2 = Coche("Ford", "Mustang")

print(coche1.presentarse())
print(coche2.presentarse())

# Cambio de cantidad de ruedas usando método de clase

Coche.cambiar_ruedas(6)

print(coche1.presentarse())
print(coche2.presentarse())

"""
Métodos de clase y de instancia:
Los métodos también pueden ser de clase o de instancia. Los métodos de clase trabajan con atributosde clase, mientras que los métodos de instancia trabajan con atributos de instancia
"""

