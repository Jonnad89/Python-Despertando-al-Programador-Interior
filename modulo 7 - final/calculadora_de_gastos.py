import os

# Función para registrar un gasto
def registrar_gasto(gastos, fecha, descripcion, cantidad):
    gastos.append({
        'fecha': fecha,
        'descripcion': descripcion,
        'cantidad': cantidad
    })

# Función para calcular el gasto total
def calcular_gasto_total(gastos):
    total = sum(gasto['cantidad'] for gasto in gastos)
    return total

# Función para mostrar la lista de gastos
def mostrar_gastos(gastos):
    print("\nLista de Gastos:")
    for gasto in gastos:
        print(f"Fecha: {gasto['fecha']}, Descripción: {gasto['descripcion']}, Cantidad: ${gasto['cantidad']:.2f}")

# Función para guardar los gastos en un archivo
def guardar_gastos(gastos, archivo):
    with open(archivo, 'w') as file:
        for gasto in gastos:
            file.write(f"{gasto['fecha']},{gasto['descripcion']},{gasto['cantidad']}\n")

# Función para cargar los gastos desde un archivo
def cargar_gastos(archivo):
    gastos = []
    if os.path.exists(archivo):
        with open(archivo, 'r') as file:
            for line in file:
                fecha, descripcion, cantidad = line.strip().split(',')
                gastos.append({
                    'fecha': fecha,
                    'descripcion': descripcion,
                    'cantidad': float(cantidad)
                })
    return gastos

def main():
    archivo_gastos = 'gastos.txt'
    gastos = cargar_gastos(archivo_gastos)
    
    while True:
        print("\nCalculadora de Gastos")
        print("1. Registrar Gasto")
        print("2. Mostrar Gastos")
        print("3. Calcular Gasto Total")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            fecha = input("Ingrese la fecha (DD-MM-YYYY): ")
            descripcion = input("Ingrese la descripción del gasto: ")
            cantidad = float(input("Ingrese la cantidad gastada: "))
            registrar_gasto(gastos, fecha, descripcion, cantidad)
            guardar_gastos(gastos, archivo_gastos)
            print("Gasto registrado con éxito.")
        
        elif opcion == '2':
            mostrar_gastos(gastos)
        
        elif opcion == '3':
            total = calcular_gasto_total(gastos)
            print(f"Gasto Total: ${total:.2f}")
        
        elif opcion == '4':
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
