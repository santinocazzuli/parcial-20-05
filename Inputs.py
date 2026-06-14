def solicitar_votos_partido(numero_partido: int) -> int:
    while True:
        entrada = input(f"Ingrese los votos para el Partido {numero_partido}: ")
        es_valido = True
        if len(entrada) == 0:
            es_valido = False
        else:
            for caracter in entrada:
                if ord(caracter) < 48 or ord(caracter) > 57:
                    es_valido = False
                    break
        if es_valido:
            votos = int(entrada)
            if votos > 0:
                return votos
            else:
                print("Error: La cantidad de votos debe ser mayor a cero.")
        else:
            print("Error invalido: Por favor, ingrese un numero entero valido (sin letras).")

def solicitar_opcion_menu() -> str:
    return input("Seleccione una opcion del menu (1-13): ")
                return numero
        print(f"Opcion invalida. Debe ser un numero entre {min_opc} and {max_opc}.")
