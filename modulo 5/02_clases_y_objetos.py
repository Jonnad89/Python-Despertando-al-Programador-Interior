class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        self.saldo += monto
        return f"Depósito exitoso. Saldo actual: {self.saldo}"

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return f"Retiro exitoso. Saldo actual: {self.saldo}"
        else: 
            return "Saldo insuficiente para realizar el retiro"


cuenta1 = CuentaBancaria("Ana", 1000)
cuenta2 = CuentaBancaria("Juan", 500)

# print(cuenta1.depositar(200))
# print(cuenta2.retirar(300))
# print(cuenta1.retirar(1500))

class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
rectangulo1 = Rectangulo(5, 3)
rectangulo2 = Rectangulo(8, 6)

area1 = rectangulo1.calcular_area()
perimetro2 = rectangulo2.calcular_perimetro()

print(f"Área del rectángulo 1: {area1}")
print(f"Perímetro del rectángulo 2: {perimetro2}")