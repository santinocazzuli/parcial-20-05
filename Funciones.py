# Funciones.py

import Prints

def calcular_total_votos(lista_votos):
    total = 0
    for i in range(len(lista_votos)):
        total += lista_votos[i]
    return total

def calcular_porcentaje(votos_partido, total_votos):
    if total_votos == 0:
        return 0.0
    return (votos_partido / total_votos) * 100

def calcular_promedio_votos(lista_votos):
    total = calcular_total_votos(lista_votos)
    if len(lista_votos) == 0:
        return 0.0
    return total / len(lista_votos)

def mostrar_segun_porcentaje(lista_id, lista_votos, limite_porcentaje, condicion):
    total_votos = calcular_total_votos(lista_votos)
    hay_datos = False   
    for i in range(len(lista_votos)):
        porcentaje = calcular_porcentaje(lista_votos[i], total_votos)
        
        if condicion == "menor" and porcentaje < limite_porcentaje:
            print(f"Partido {lista_id[i]} -> Votos: {lista_votos[i]} | Porcentaje: {porcentaje:.2f}%")
            hay_datos = True
        elif condicion == "mayor" and porcentaje > limite_porcentaje:
            print(f"Partido {lista_id[i]} -> Votos: {lista_votos[i]} | Porcentaje: {porcentaje:.2f}%")
            hay_datos = True
            
    if not hay_datos:
        print(f"No se encontraron partidos con la condicion solicitada.")

def mostrar_segun_cantidad_votos(lista_id, lista_votos, limite_votos):
    total_votos = calcular_total_votos(lista_votos)
    hay_datos = False
    
    for i in range(len(lista_votos)):
        if lista_votos[i] > limite_votos:
            porcentaje = calcular_porcentaje(lista_votos[i], total_votos)
            print(f"Partido {lista_id[i]} -> Votos: {lista_votos[i]} | Porcentaje: {porcentaje:.2f}%")
            hay_datos = True
            
    if not hay_datos:
        print(f"No hay partidos con mas de {limite_votos} votos.")

def mostrar_por_encima_del_promedio(lista_id, lista_votos):
    promedio = calcular_promedio_votos(lista_votos)
    total_votos = calcular_total_votos(lista_votos)
    print(f"El promedio de votos es: {promedio:.2f}")
    
    hay_datos = False
    for i in range(len(lista_votos)):
        if lista_votos[i] > promedio:
            porcentaje = calcular_porcentaje(lista_votos[i], total_votos)
            print(f"Partido {lista_id[i]} -> Votos: {lista_votos[i]} | Porcentaje: {porcentaje:.2f}%")
            hay_datos = True
            
    if not hay_datos:
        print("Ningun partido supera el promedio.")

def encontrar_partido_menos_votado(lista_id, lista_votos):
    if len(lista_votos) == 0:
        print("No hay datos cargados.")
        return
    menor_votos = lista_votos[0]
    indice_menor = 0

    for i in range(1, len(lista_votos)):
        if lista_votos[i] < menor_votos:
            menor_votos = lista_votos[i]
            indice_menor = i
        elif lista_votos[i] == menor_votos:
            if len(lista_id[i]) < len(lista_id[indice_menor]):
                menor_votos = lista_votos[i]
                indice_menor = i

    total_votos = calcular_total_votos(lista_votos)
    porcentaje = calcular_porcentaje(menor_votos, total_votos)
    
    print("\n--- Partido Menos Votado ---")
    print(f"Partido: {lista_id[indice_menor]} | Votos: {menor_votos} | Porcentaje: {porcentaje:.2f}%")

def verificar_segunda_vuelta(lista_id, lista_votos, cantidad_partidos):
    total_votos = calcular_total_votos(lista_votos, cantidad_partidos)
    if total_votos == 0:
        print("No hay votos registrados.")
        return

    votos_aux = [0] * cantidad_partidos
    id_aux = [None] * cantidad_partidos
    for i in range(cantidad_partidos):
        votos_aux[i] = lista_votos[i]
        id_aux[i] = lista_id[i]
    max_1 = votos_aux[0]
    idx_1 = 0
    for i in range(1, cantidad_partidos):
        if votos_aux[i] > max_1:
            max_1 = votos_aux[i]
            idx_1 = i

    partido_1 = id_aux[idx_1]
    porcentaje_1 = calcular_porcentaje(max_1, total_votos)
    max_2 = -1
    partido_2 = "Ninguno"
    for i in range(cantidad_partidos):
        if i != idx_1:
            if max_2 == -1 or votos_aux[i] > max_2:
                max_2 = votos_aux[i]
                partido_2 = id_aux[i]

    print(f"\nPartido ganador en votos: {partido_1} con el {porcentaje_1:.2f}%")

    if porcentaje_1 > 45.0:
        print("NO HAY SEGUNDA VUELTA. Gana el primer partido por superar el 45%.")
    elif porcentaje_1 >= 40.0:
        porcentaje_2 = calcular_porcentaje(max_2, total_votos) if partido_2 != "Ninguno" else 0.0
        diferencia = porcentaje_1 - porcentaje_2
        if diferencia > 10.0:
            print("NO HAY SEGUNDA VUELTA. Gana por superar el 40% con mas de 10% de diferencia.")
        else:
            print(f"HAY SEGUNDA VUELTA entre {partido_1} y {partido_2}. Diferencia menor al 10%.")
    else:
        print(f"HAY SEGUNDA VUELTA entre {partido_1} y {partido_2}. El ganador no llego al 40%.")

def ordenar_partidos_por_nombre(lista_id, lista_votos, cantidad_partidos):
    id_ordenado = [None] * cantidad_partidos
    votos_ordenado = [0] * cantidad_partidos
    for i in range(cantidad_partidos):
        id_ordenado[i] = lista_id[i]
        votos_ordenado[i] = lista_votos[i]
    for i in range(cantidad_partidos - 1):
        for j in range(0, cantidad_partidos - i - 1):
            if id_ordenado[j] > id_ordenado[j + 1]:
                aux_id = id_ordenado[j]
                id_ordenado[j] = id_ordenado[j + 1]
                id_ordenado[j + 1] = aux_id
                aux_votos = votos_ordenado[j]
                votos_ordenado[j] = votos_ordenado[j + 1]
                votos_ordenado[j + 1] = aux_votos

    total_votos = calcular_total_votos(votos_ordenado, cantidad_partidos)
    print("\n--- Partidos Ordenados Alfabeticamente ---")
    for i in range(cantidad_partidos):
        porcentaje = calcular_porcentaje(votos_ordenado[i], total_votos)
        Prints.mostrar_fila_partido(id_ordenado[i], votos_ordenado[i], porcentaje)