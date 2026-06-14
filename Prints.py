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

def mostrar_resultado_filtro(titulo: str, partidos: list, votos: list, porcentajes: list, resumen: str = "") -> None:
    print(f"\n--- {titulo} ---")
    print(f"{'Identificador':<15}{'Votos':<12}{'Porcentaje':<12}")
    print("-"*40)
    for i in range(len(partidos)):
        print(f"Partido {partidos[i]:<8}{votos[i]:<12}{porcentajes[i]:.2f}%")
    if resumen != "":
        print("-"*40)
        print(resumen)
