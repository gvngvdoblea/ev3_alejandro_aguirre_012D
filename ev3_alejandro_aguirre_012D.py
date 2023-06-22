import random

clientes = []

def validar_rut(rut):
    rut = rut.replace("-", "").replace(".", "")
    if len(rut) < 8 or len(rut) > 9 or not rut.isalnum():
        return False
    return True

def registrar_cliente():
    rut = input("Ingrese el Rut del cliente (sin guiones ni puntos): ")
    while not validar_rut(rut):
        print("Rut inválido. Debe tener entre 8 y 9 caracteres alfanuméricos.")
        rut = input("Ingrese nuevamente el Rut del cliente: ")

    nombre = input("Ingrese el nombre del cliente: ")
    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Ingrese nuevamente el nombre del cliente: ")

    proyecto = input("Ingrese el proyecto (VS/VF/VN): ")
    while proyecto not in ["VS", "VF", "VN"]:
        print("Proyecto inválido. Debe ser 'VS', 'VF' o 'VN'.")
        proyecto = input("Ingrese nuevamente el proyecto (VS/VF/VN): ")

    renta = float(input("Ingrese la renta mensual del cliente: "))

    cliente = {
        "rut": rut,
        "nombre": nombre,
        "proyecto": proyecto,
        "renta": renta
    }
    clientes.append(cliente)
    print("Cliente registrado con éxito.")

def buscar_por_rut():
    rut_buscar = input("Ingrese el Rut del cliente a buscar: ")
    for cliente in clientes:
        if cliente["rut"] == rut_buscar:
            print("Datos del cliente:")
            print("Rut:", cliente["rut"])
            print("Nombre:", cliente["nombre"])
            print("Proyecto:", cliente["proyecto"])
            print("Renta Mensual:", cliente["renta"])
            return
    print("No se encontró ningún cliente con ese Rut.")

def generar_reporte():
    reportes = 0
    print("Reporte IMMO Ltda.:")
    for cliente in clientes:
        if cliente["renta"] > 900000:
            print("Sr/a", cliente["nombre"])
            print("Rut:", cliente["rut"])
            print("Con su renta de", cliente["renta"])
            print("En el Proyecto:", cliente["proyecto"])
            print("Puede acceder a un Dpto de UF", random.randint(2500, 3700))
            print()
            reportes += 1
    print("Se generaron", reportes, "reportes.")

while True:
    print("Menú de registro de clientes:")
    print("1. Grabar/Registrar")
    print("2. Buscar por Rut")
    print("3. Reporte según renta")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_cliente()
    elif opcion == "2":
        buscar_por_rut()
    elif opcion == "3":
        generar_reporte()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

