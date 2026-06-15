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
            
        elif opcion == "3":
            res = funciones.filtrar_por_debajo_porcentaje(votos_partidos, 10.0)
            prints.mostrar_resultado_filtro_debajo("Partidos con menos del 10%", res)
            
        elif opcion == "4":
            res = funciones.filtrar_por_debajo_porcentaje(votos_partidos, 15.0)
            prints.mostrar_resultado_filtro_debajo("Partidos con menos del 15%", res)
            
        elif opcion == "5":
            res = funciones.filtrar_por_debajo_porcentaje(votos_partidos, 20.0)
            prints.mostrar_resultado_filtro_debajo("Partidos con menos del 20%", res)
            
        elif opcion == "6":
            res = funciones.filtrar_por_encima_votos(votos_partidos, 500)
            prints.mostrar_resultado_filtro_encima("Partidos con mas de 500 votos", res, 500)
            
        elif opcion == "7":
            res = funciones.filtrar_por_encima_votos(votos_partidos, 1000)
            prints.mostrar_resultado_filtro_encima("Partidos con mas de 1000 votos", res, 1000)
            
        elif opcion == "8":
            promedio_gral = funciones.calcular_promedio_votos(votos_partidos)
            res = funciones.filtrar_por_encima_votos(votos_partidos, int(promedio_gral))
            prints.mostrar_resultado_promedio(res, promedio_gral, votos_partidos)
            
        elif opcion == "9":
            res = funciones.obtener_partidos_menos_votados(votos_partidos)
            prints.mostrar_resultado_menos_votado(res)
            
        elif opcion == "10":
            res = funciones.evaluar_segunda_vuelta_logica(votos_partidos)
            if res[0]:
                print("\nResultado: DEBE REALIZARSE UNA SEGUNDA VUELTA ELECTORAL.")
                print(f"partido mas votado -> Partido {res[1]} | Votos: {res[2]} ({res[3]:.2f}%)")
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
            prints.mostrar_nombres_ordenados(nombres_ordenados)
            
        elif opcion == "13":
            print("\nMuchas gracias por utilizar nuestro sistema. Finalizando programa...")
            break
        else:
            prints.mostrar_mensaje_error("Opcion invalida. Ingrese un numero correspondiente a las opciones (1-13).")
