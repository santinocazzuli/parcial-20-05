#Menu.py

import Prints
import Inputs
import Funciones

def ejecutar_menu():
    lista_id = []
    lista_votos = []
    datos_cargados = False

    while True:
        Prints.mostrar_menu_principal()
        opcion = Inputs.pedir_opcion_menu("Seleccione una opcion (1-13): ", 1, 13)

        if opcion >= 2 and opcion <= 10 and not datos_cargados:
            Prints.mostrar_error("Debe cargar datos primero (Opcion 1 o Opcion 11).")
            continue

        if opcion == 1:
            print("\n--- Carga de Votos ---")
            lista_id = []
            lista_votos = []
            cantidad = Inputs.pedir_entero("Ingrese la cantidad de partidos a cargar: ", "Error. Debe ingresar un numero entero mayor a cero.")
            
            for i in range(cantidad):
                print(f"\nDatos del partido {i + 1}:")
                while True:
                    nombre = input("Ingrese el nombre del partido: ")
                    if len(nombre) > 0:
                        break
                    print("Error. El nombre no puede estar vacio.")
                
                votos = Inputs.pedir_entero(f"Ingrese los votos para {nombre}: ", "Error. Los votos deben ser un numero entero mayor a cero.")
                
                lista_id.append(nombre)
                lista_votos.append(votos)
            
            datos_cargados = True
            print("\nDatos cargados con exito.")

        elif opcion == 2:
            print("\n- Lista de Votos Emitidos -")
            total_votos = Funciones.calcular_total_votos(lista_votos)
            for i in range(len(lista_votos)):
                porcentaje = Funciones.calcular_porcentaje(lista_votos[i], total_votos)
                Prints.mostrar_fila_partido(lista_id[i], lista_votos[i], porcentaje)

        elif opcion == 3:
            print("\n- Partidos con menos del 10% de votos -")
            Funciones.mostrar_segun_porcentaje(lista_id, lista_votos, 10.0, "menor")

        elif opcion == 4:
            print("\n- Partidos con menos del 15% de votos -")
            Funciones.mostrar_segun_porcentaje(lista_id, lista_votos, 15.0, "menor")

        elif opcion == 5:
            print("\n- Partidos con menos del 20% de votos -")
            Funciones.mostrar_segun_porcentaje(lista_id, lista_votos, 20.0, "menor")

        elif opcion == 6:
            print("\n- Partidos con mas de 500 votos -")
            Funciones.mostrar_segun_cantidad_votos(lista_id, lista_votos, 500)

        elif opcion == 7:
            print("\n- Partidos con mas de 1000 votos -")
            Funciones.mostrar_segun_cantidad_votos(lista_id, lista_votos, 1000)

        elif opcion == 8:
            print("\n- Partidos por encima del promedio -")
            Funciones.mod_por_encima_del_promedio = Funciones.mostrar_por_encima_del_promedio(lista_id, lista_votos)

        elif opcion == 9:
            Funciones.encontrar_partido_menos_votado(lista_id, lista_votos)

        elif opcion == 10:
            Funciones.verificar_segunda_vuelta(lista_id, lista_votos)

        elif opcion == 11:
            print("\n- Hardcodeando vectores (10 partidos) -")
            lista_id = ["Partido A", "Partido B", "Partido C", "Partido D", "Partido E", "Partido F", "Partido G", "Partido H", "Partido I", "Partido J"]
            lista_votos = [1200, 450, 800, 150, 2300, 600, 90, 1100, 350, 750]
            datos_cargados = True
            print("Se cargaron 10 partidos de prueba correctamente.")

        elif opcion == 12:
            if not datos_cargados:
                Prints.mostrar_error("Debe cargar datos primero (Opcion 1 o Opcion 11).")
            else:
                Funciones.ordenar_partidos_por_nombre(lista_id, lista_votos)

        elif opcion == 13:
            print("\nGracias por utilizar el sistema. Saliendo...")
            break