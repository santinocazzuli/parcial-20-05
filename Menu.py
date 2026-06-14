import inputs
import funciones
import prints

def ejecutar_sistema() -> None:
    votos_partidos = []
    datos_cargados = False
    while True:
        prints.mostrar_menu_opciones()
        opcion = inputs.solicitar_opcion_menu()
        if opcion != "1" and opcion != "11" and opcion != "12" and opcion != "13" and not datos_cargados:
            prints.mostrar_mensaje_error("Acceso denegado. Primero debe cargar los votos (Opcion 1 o 11).")
            continue
        if opcion == "1":
            votos_partidos = inputs.cargar_votos_secuenciales()
            datos_cargados = True
            print("Carga masiva completada con exito!")
        elif opcion == "2":
            prints.mostrar_listado_general(votos_partidos)
        elif opcion in ["3", "4", "5"]:
            limite = 10.0 if opcion == "3" else (15.0 if opcion == "4" else 20.0)
            res = funciones.filtrar_por_debajo_porcentaje(votos_partidos, limite)
            if len(res[0]) == 0:
                prints.mostrar_mensaje_error(f"No se registraron partidos con menos del {limite}% de los votos.")
            else:
                resumen = f"Porcentaje acumulado de la busqueda: {res[3]:.2f}%"
                prints.mostrar_resultado_filtro(f"Partidos con menos del {limite}%", res[0], res[1], res[2], resumen)
        elif opcion in ["6", "7"]:
            limite_votos = 500 if opcion == "6" else 1000
            res = funciones.filtrar_por_encima_votos(votos_partidos, limite_votos)
            if len(res[0]) == 0:
                prints.mostrar_mensaje_error(f"No hay partidos politicos con mas de {limite_votos} votos.")
            else:
                suma_votos = funciones.calcular_total_votos(res[1])
                cant_partidos = len(res[0])
                promedio_votos = suma_votos / cant_partidos
                resumen = f"Suma de votos: {suma_votos} | Cantidad: {cant_partidos} | Promedio: {promedio_votos:.2f}"
                prints.mostrar_resultado_filtro(f"Partidos con mas de {limite_votos} votos", res[0], res[1], res[2], resumen)
        elif opcion == "8":
            promedio_gral = funciones.calcular_promedio_votos(votos_partidos)
            res = funciones.filtrar_por_encima_votos(votos_partidos, int(promedio_gral))
            if len(res[0]) == 0:
                prints.mostrar_mensaje_error("Ningun partido supero el promedio general.")
            else:
                total_filtrados = funciones.calcular_total_votos(res[1])
                total_global = funciones.calcular_total_votos(votos_partidos)
                porcentaje_acum = (total_filtrados / total_global) * 100
                resumen = f"Promedio general de votos: {promedio_gral:.2f}\nPorcentaje acumulado encontrado: {porcentaje_acum:.2f}%"
                prints.mostrar_resultado_filtro("Partidos por encima del promedio general", res[0], res[1], res[2], resumen)
        elif opcion == "9":
            res = funciones.obtener_partidos_menos_votados(votos_partidos)
            prints.mostrar_resultado_filtro("Partido menos votado de la eleccion", res[0], res[1], res[2])
            if len(res[0]) > 1:
                print(f"[PUNTO EXTRA] Se detecto un empate multiple entre {len(res[0])} partidos!")
        elif opcion == "10":
            res = funciones.evaluar_segunda_vuelta_logica(votos_partidos)
            if res[0]:
                print("\nResultado: DEBE REALIZARSE UNA SEGUNDA VUELTA ELECTORAL.")
            else:
                print("\nResultado: NO DEBE REALIZARSE UNA SEGUNDA VUELTA ELECTORAL.")
                print(f"Ganador definitivo -> Partido {res[1]} | Votos: {res[2]} ({res[3]:.2f}%)")
        elif opcion == "11":
            votos_partidos = [888, 555, 333, 1850, 999, 777, 1400, 180, 2500, 60]
            datos_cargados = True
            print("\n[INFO] Vector modificado. Se han cargado exitosamente los 10 partidos hardcodeados.")
        elif opcion == "12":
            lista_nombres = ["Frente UTN", "Alianza Scarafilo", "La libertad de Baus", "Unidad de Python", "Frente de Java"]
            print("\n--- PUNTO 12: ORDENAMIENTO DE NOMBRES DE PARTIDOS (PUNTO AISLADO) ---")
            print("Arreglo original hardcodeado:")
            print(lista_nombres)
            nombres_ordenados = funciones.ordenar_nombres_alfabeticamente(lista_nombres)
            print("\nArreglo ordenado alfabeticamente (A-Z):")
            for nombre in nombres_ordenados:
                print(f"- {nombre}")
        elif opcion == "13":
            print("\nMuchas gracias por utilizar nuestro sistema. Finalizando programa...")
            break
        else:
            prints.mostrar_mensaje_error("Opcion invalida. Ingrese un numero correspondiente a las opciones (1-13).")
