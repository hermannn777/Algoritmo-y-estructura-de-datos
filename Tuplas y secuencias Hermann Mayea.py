from os import system, name
from time import sleep


estudiantes = []
os = name

while True:
    print("\n--- SISTEMA DE GESTIÓN DE ESTUDIANTES ---")
    print("1. Registrar nuevo estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Calcular promedio general")
    print("4. Buscar estudiante por nombre")
    print("5. Mostrar estudiantes con nota mayor al promedio")
    print("6. Mostrar mejor y peor nota")
    print("7. Eliminar estudiante por nombre")
    print("8. Salir")

    opcion = input("Elige una opción: ")
    
    match opcion:
        case "1":
            nombre = input("Nombre del estudiante: ")
            try:
                edad = int(input("Edad: "))
                nota = float(input("Nota (0-10): "))
            except ValueError:
                print("Edad o nota inválidas. Intenta de nuevo.")
                continue

            if edad <= 0 or nota < 0 or nota > 10:
                print("Datos inválidos. Intenta de nuevo.")
            else:
                nuevo_estudiante = {
                    "nombre": nombre,
                    "edad": edad,
                    "nota": nota
                }
                estudiantes.append(nuevo_estudiante)
                print(f"Estudiante {nombre} registrado con éxito.")

        case "2":
            if not estudiantes:
                print("No hay estudiantes registrados aún.")
            else:
                print("\nEstudiantes registrados:")
                print("-------------------------")
                for i, estudiante in enumerate(estudiantes, 1):
                    print(f"{i}. Nombre: {estudiante['nombre']}")
                    print(f"   Edad: {estudiante['edad']}")
                    print(f"   Nota: {estudiante['nota']}")
                    print("-------------------------")
                print(estudiantes)
                print(type(estudiantes))
        case "3":
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                suma_notas = sum(e["nota"] for e in estudiantes)
                promedio = suma_notas / len(estudiantes)
                print(f"El promedio general de notas es: {promedio:.2f}")
        case "4":
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                encontrar = input("Nombre del estudiante: ")

                for e in estudiantes:
                    if encontrar == e["nombre"]:
                        print("Estudiante encontrado:")
                        print(f"\tNombre: {e['nombre']}")
                        print(f"\tEdad: {e['edad']}")
                        print(f"\tNota: {e['nota']}")
                        break
                else:
                    print("No hay un estudiante registrado con ese nombre.")
                    
        case "5":
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else: 
                suma_notas = sum(e["nota"] for e in estudiantes)
                promedio = suma_notas / len(estudiantes)
                print(f"El promedio general de notas es: {promedio:.2f}")
                print("Los estudiantes por encima del promedio son: ")
                booleano = False
                for p in estudiantes:
                    if p["nota"] > promedio:
                        print(f"\tNombre: {p['nombre']}")
                        print(f"\tEdad: {p['edad']}")
                        print(f"\tNota: {p['nota']}")
                        booleano = True
                if not booleano:
                    print("No hay estudiantes con una nota por encima del promedio")

        case "6":
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                mejor = estudiantes[0]
                peor = estudiantes[0]

                for p in estudiantes:
                    if p["nota"] > mejor["nota"]:
                        mejor = p
                    if p["nota"] < peor["nota"]:
                        peor = p
                
                print("Estudiante con la mejor nota:")
                print(f"\tNombre: {mejor['nombre']}")
                print(f"\tEdad: {mejor['edad']}")
                print(f"\tNota: {mejor['nota']}")

                print("Estudiante con la peor nota:")
                print(f"\tNombre: {peor['nombre']}")
                print(f"\tEdad: {peor['edad']}")
                print(f"\tNota: {peor['nota']}")
                
        case "7":
            eliminar = str(input("Ponga el nombre del estudiante que quiere eliminar: "))

            for i, nombre in enumerate(estudiantes):
                if eliminar == nombre["nombre"]:
                    estudiantes.pop(i)
                    print("Estudiante eliminado")
                    continue

        case "8":
            print("Saliendo del programa...")
            break

        case _:
            print("Opción no válida. Intenta otra vez.")

    sleep(3)
    if os == "nt":
        system("cls")
    else:
        system("clear")
