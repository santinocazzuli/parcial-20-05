#Inputs.py

def es_numero_valido(cadena):

    if len(cadena) == 0:
        return False
    
    for i in range(len(cadena)):
        caracter = cadena[i]
        if caracter < '0' or caracter > '9':
            return False
    return True

def convertir_a_entero(cadena):
    numero = 0
    for i in range(len(cadena)):
        digito = ord(cadena[i]) - ord('0')
        numero = numero * 10 + digito
    return numero

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
        print(f"Opcion invalida. Debe ser un numero entre {min_opc} y {max_opc}.")