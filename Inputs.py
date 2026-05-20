# inputs.py

def es_numero_valido(cadena):
    if len(cadena) == 0:
        return False
    digitos_validos = "0123456789"
    
    for i in range(len(cadena)):
        caracter = cadena[i]
        encontrado = False
        for j in range(len(digitos_validos)):
            if caracter == digitos_validos[j]:
                encontrado = True
                break
        if not encontrado:
            return False
    return True

def convertir_a_entero(cadena):
    digitos_validos = "0123456789"
    numero_final = 0
    for i in range(len(cadena)):
        caracter_actual = cadena[i]
        valor_digito = 0
        for j in range(len(digitos_validos)):
            if caracter_actual == digitos_validos[j]:
                valor_digito = j
                break
        numero_final = numero_final * 10 + valor_digito
        
    return numero_final

def pedir_entero(mensaje, mensaje_error):
    while True:
        entrada = input(mensaje)
        if es_numero_valido(entrada):
            numero = convertir_a_entero(entrada)
            if numero > 0:
                return numero
        print(mensaje_error)

def pedir_opcion_menu(mensaje, min_opc, max_opc):
    while True:
        entrada = input(mensaje)
        if es_numero_valido(entrada):
            numero = convertir_a_entero(entrada)
            if numero >= min_opc and numero <= max_opc:
                return numero
        print(f"Opcion invalida. Debe ser un numero entre {min_opc} and {max_opc}.")