import funciones

def mostrar_menu_opciones() -> None:
    print("\n" + "="*50)
    print("      SISTEMA DE GESTION DE ELECCIONES UTN FRA      ")
    print("="*50)
    print("1. Cargar votos (5 partidos iniciales)")
    print("2. Mostrar votos generales y porcentajes")
    print("3. Partidos con menos del 10% de votos")
    print("4. Partidos con menos del 15% de votos")
    print("5. Partidos con menos del 20% de votos")
    print("6. Partidos con mas de 500 votos")
    print("7. Partidos con mas de 1000 votos")
    print("8. Partidos por encima del promedio general")
    print("9. Identificar al Partido menos votado (con empates)")
    print("10. Verificar necesidad de Segunda Vuelta (Ballotaje)")
    print("11. Hardcodear vector (Cargar datos de prueba: 10 partidos)")
    print("12. Ordenar partidos politicos por nombre (Punto Aislado)")
    print("13. Salir")
    print("="*50)

def mostrar_mensaje_error(mensaje: str) -> None:
    print(f"\n[ERROR] {mensaje}")

def mostrar_listado_general(votos_partidos: list) -> None:
    total = funciones.calcular_total_votos(votos_partidos)
    cantidad = len(votos_partidos)
    print(f"\n--- LISTADO GENERAL DE VOTOS (Cantidad de Partidos Postulados: {cantidad}) ---")
    print(f"{'Identificador':<15}{'Votos':<12}{'Porcentaje':<12}")
    print("-"*40)
    for i in range(cantidad):
        porcentaje = (votos_partidos[i] / total) * 100
        print(f"Partido {i+1:<8}{votos_partidos[i]:<12}{porcentaje:.2f}%")
    print("-"*40)
    print(f"TOTAL GENERAL DE VOTOS ACUMULADOS: {total}")

def mostrar_resultado_filtro_debajo(titulo: str, res_funciones: tuple) -> None:
    partidos, votos, porcentajes, porcentaje_acumulado = res_funciones
    if len(partidos) == 0:
        print(f"\n[ERROR] No se registraron partidos para este filtro.")
        return
    print(f"\n--- {titulo} ---")
    print(f"{'Identificador':<15}{'Votos':<12}{'Porcentaje':<12}")
    print("-"*40)
    for i in range(len(partidos)):
        print(f"Partido {partidos[i]:<8}{votos[i]:<12}{porcentajes[i]:.2f}%")
    print("-"*40)
    print(f"Porcentaje acumulado de la busqueda: {porcentaje_acumulado:.2f}%")

def mostrar_resultado_filtro_encima(titulo: str, res_funciones: tuple, limite_votos: int) -> None:
    partidos, votos, porcentajes = res_funciones
    if len(partidos) == 0:
        print(f"\n[ERROR] No hay partidos politicos con mas de {limite_votos} votos.")
        return
    print(f"\n--- {titulo} ---")
    print(f"{'Identificador':<15}{'Votos':<12}{'Porcentaje':<12}")
    print("-"*40)
    for i in range(len(partidos)):
        print(f"Partido {partidos[i]:<8}{votos[i]:<12}{porcentajes[i]:.2f}%")
    print("-"*40)
    suma_votos = funciones.calcular_total_votos(votos)
    cant_partidos = len(partidos)
    promedio_votos = suma_votos / cant_partidos
    print(f"Suma de votos: {suma_votos} | Cantidad: {cant_partidos} | Promedio: {promedio_votos:.2f}")

def mostrar_resultado_promedio(res_funciones: tuple, promedio_gral: float, votos_partidos: list) -> None:
    partidos, votos, porcentajes = res_funciones
    if len(partidos) == 0:
        print("\n[ERROR] Ningun partido supero el promedio general.")
        return
    print(f"\n--- Partidos por encima del promedio general ---")
    print(f"{'Identificador':<15}{'Votos':<12}{'Porcentaje':<12}")
    print("-"*40)
    for i in range(len(partidos)):
        print(f"Partido {partidos[i]:<8}{votos[i]:<12}{porcentajes[i]:.2f}%")
    print("-"*40)
    total_filtrados = funciones.calcular_total_votos(votos)
    total_global = funciones.calcular_total_votos(votos_partidos)
    porcentaje_acum = (total_filtrados / total_global) * 100
    print(f"Promedio general de votos: {promedio_gral:.2f}")
    print(f"Porcentaje acumulado encontrado: {porcentaje_acum:.2f}%")

def mostrar_resultado_menos_votado(res_funciones: tuple) -> None:
    partidos, votos, porcentajes = res_funciones
    print(f"\n--- Partido menos votado de la eleccion ---")
    print(f"{'Identificador':<15}{'Votos':<12}{'Porcentaje':<12}")
    print("-"*40)
    for i in range(len(partidos)):
        print(f"Partido {partidos[i]:<8}{votos[i]:<12}{porcentajes[i]:.2f}%")
    if len(partidos) > 1:
        print(f"[PUNTO EXTRA] Se detecto un empate multiple entre {len(partidos)} partidos!")

def mostrar_nombres_ordenados(nombres_ordenados: list) -> None:
    print("\nArreglo ordenado alfabeticamente (A-Z):")
    for nombre in nombres_ordenados:
        print(f"- {nombre}")
