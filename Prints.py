#Prints.py

def mostrar_menu_principal():
    print("\n" + "="*40)
    print("   SISTEMA DE GESTION DE ELECCIONES UTN")
    print("="*40)
    print("1. Cargar votos")
    print("2. Mostrar votos")
    print("3. Partidos con menos del 10% de votos")
    print("4. Partidos con menos del 15% de votos")
    print("5. Partidos con menos del 20% de votos")
    print("6. Partidos con mas de 500 votos")
    print("7. Partidos con mas de 1000 votos")
    print("8. Partidos por encima del promedio")
    print("9. Partido menos votado")
    print("10. Verificar segunda vuelta")
    print("11. Hardcodear vector (10 partidos)")
    print("12. Ordenar partidos políticos por nombre")
    print("13. Salir")
    print("="*40)

def mostrar_error(mensaje):
    print(f"ERROR: {mensaje}")

def mostrar_fila_partido(identificador, votos, porcentaje):
    print(f"Partido {identificador} -> Votos: {votos} | Porcentaje: {porcentaje:.2f}%")