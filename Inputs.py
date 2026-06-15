def solicitar_votos_partido(numero_partido: int) -> int:
    while True:
        entrada = input(f"Ingrese los votos para el Partido {numero_partido}: ")
        es_valido = True
        if len(entrada) == 0:
            es_valido = False
        else:
            for caracter in entrada:
                caracteres_validos = "0123456789"
                pertenece = False
                for digito in caracteres_validos:
                    if caracter == digito:
                        pertenece = True
                        break
                if not pertenece:
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

def cargar_votos_secuenciales() -> list:
    lista_votos = [0] * 5
    print("\n--- INICIO DE CARGA SECUENCIAL DE VOTOS ---")
    for i in range(5):
        voto_validado = solicitar_votos_partido(i + 1)
        lista_votos[i] = voto_validado
    return lista_votos

def solicitar_opcion_menu() -> str:
    return input("Seleccione una opcion del menu (1-13): ")
