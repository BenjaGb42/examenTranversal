import random
import math
import csv
import os 
# Lista de empleados;
empleados = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

# Función principal:
def main():
    sueldos = []  # Lista vacía para almacenar los sueldos:

#Menú de Opciones:
    while True:
        print("\n******** Menú de Opciones ********")
        print("===================================")
        print("1 .- Asignar sueldos aleatorios")
        print("2 .- Clasificar sueldos")
        print("3 .- Ver estadísticas")
        print("4 .- Reporte de sueldos")
        print("5 .- Salir del programa")

        try:
            opcion = int(input("Ingrese la opción que desea : "))
        except ValueError:
            print("Debe ser un número entero, entre 1 y 5.")
            continue

        if opcion == 1:
            sueldos = Generar_Sueldos()
            print("Los sueldos han sido asignados correctamente.")
        elif opcion == 2:
            if not sueldos:
                print("Primero debe asignar los sueldos aleatorios.")
                continue
            clasificacion = Clasificar_Sueldos(sueldos, empleados)
            Mostrar_Clasificacion(clasificacion)
        elif opcion == 3:
            if not sueldos:
                print("Primero debe asignar sueldos aleatorios.")
                continue
            Ver_Estadisticas(sueldos)
        elif opcion == 4:
            if not sueldos:
                print("Primero debe asignar sueldos aleatorios.")
                continue
            detalles = Calcular_Sueldo_Liquido(sueldos, empleados)
            for detalle in detalles:
                print(f"{detalle[0]}: Sueldo Base: ${detalle[1]}, Descuento Salud: ${detalle[2]}, Descuento AFP: ${detalle[3]}, Sueldo Líquido: ${detalle[4]}")
        elif opcion == 5:
            print("Finalizando el programa...")
            print("Desarrollado por Benjamin Erpel Avendaño")
            print("RUT 21.685.054-8")
            break
        else:
            print("Opción inválida, debe ser entre 1 y 5.")

# Función para la generacin de sueldos aleatorios:
def Generar_Sueldos():
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    return sueldos

# Función para la clasificacioin de sueldos:
def Clasificar_Sueldos(sueldos, empleados):
    clasificacion = {
        'menores_800': [],
        'entre_800_y_2000': [],
        'mayores_2000': []
    }
    for sueldo, empleado in zip(sueldos, empleados):
        if sueldo < 800000:
            clasificacion['menores_800'].append((empleado, sueldo))
        elif 800000 <= sueldo <= 2000000:
            clasificacion['entre_800_y_2000'].append((empleado, sueldo))
        else:
            clasificacion['mayores_2000'].append((empleado, sueldo))
    return clasificacion

# Función para mostrar la  clasificación de sueldos:
def Mostrar_Clasificacion(clasificacion):
    print("Sueldos menores a $800.000")
    print(f"TOTAL: {len(clasificacion['menores_800'])}")
    for empleado, sueldo in clasificacion['menores_800']:
        print(f"{empleado}: ${sueldo}")

    print("\nSueldos entre $800.000 y $2.000.000")
    print(f"TOTAL: {len(clasificacion['entre_800_y_2000'])}")
    for empleado, sueldo in clasificacion['entre_800_y_2000']:
        print(f"{empleado}: ${sueldo}")

    print("\nSueldos superiores a $2.000.000")
    print(f"TOTAL: {len(clasificacion['mayores_2000'])}")
    for empleado, sueldo in clasificacion['mayores_2000']:
        print(f"{empleado}: ${sueldo}")

    total_sueldos = sum(sueldo for clasif in clasificacion.values() for _, sueldo in clasif)
    print(f"\nTOTAL SUELDOS: ${total_sueldos}")

#Función para mostrar  estadísticas:
def Ver_Estadisticas(sueldos):
    sueldo_mas_alto = (sueldos)
    sueldo_mas_bajo = (sueldos)
    promedio_sueldos = sum(sueldos) / len(sueldos)
    media_geometrica = calcular_media_geometrica(sueldos)

    print(f"Sueldo más alto: ${sueldo_mas_alto}")
    print(f"Sueldo más bajo: ${sueldo_mas_bajo}")
    print(f"Promedio de sueldos: ${promedio_sueldos}")
    print(f"Media geométrica: ${media_geometrica:.2f}")

# Función para calcular la media geométrica:
def calcular_media_geometrica(datos):
    producto = 1
    for dato in datos:
        producto *= dato
    media_geom = producto ** (1 / len(datos))
    return media_geom

#Función de reporte de sueldos para calcular descuentos y sueldo líquido:
def Calcular_Sueldo_Liquido(sueldos, empleados):
    detalles = []
    for sueldo, empleado in zip(sueldos, empleados):
        descuento_salud = sueldo * 0.07
        descuento_afp = sueldo * 0.12
        sueldo_liquido = sueldo - descuento_salud - descuento_afp
        detalles.append((empleado, sueldo, descuento_salud, descuento_afp, sueldo_liquido))
    return detalles

# Función para exportar los  datos a CSV:
def exportar_a_csv(detalles):
    with open('sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "S Líquido"])
        for detalle in detalles:
            writer.writerow(detalle)
    print("Datos exportados correctamente a sueldos.csv")

# Ejecución del programa :),<3
main()
