def calcular_total_votos(lista: list) -> int:
    total = 0
    for votos in lista:
        total += votos
    return total

def calcular_promedio_votos(lista: list) -> float:
    total = calcular_total_votos(lista)
    if len(lista) == 0:
        return 0.0
    return total / len(lista)

def encontrar_menor_voto(lista: list) -> int:
    menor = lista[0]
    for votos in lista:
        if votos < menor:
            menor = votos
    return menor

def encontrar_mayor_voto(lista: list) -> int:
    mayor = lista[0]
    for votos in lista:
        if votos > mayor:
            mayor = votos
    return mayor

def filtrar_por_debajo_porcentaje(votos: list, limite: float) -> tuple:
    total_votos = calcular_total_votos(votos)
    cantidad_cumplen = 0
    for i in range(len(votos)):
        porcentaje = (votos[i] / total_votos) * 100
        if porcentaje < limite:
            cantidad_cumplen += 1
    partidos_filtrados = [0] * cantidad_cumplen
    votos_filtrados = [0] * cantidad_cumplen
    porcentajes_filtrados = [0.0] * cantidad_cumplen
    porcentaje_acumulado = 0.0
    indice = 0
    for i in range(len(votos)):
        porcentaje = (votos[i] / total_votos) * 100
        if porcentaje < limite:
            partidos_filtrados[indice] = i + 1
            votos_filtrados[indice] = votos[i]
            porcentajes_filtrados[indice] = porcentaje
            porcentaje_acumulado += porcentaje
            indice += 1
            
    return (partidos_filtrados, votos_filtrados, porcentajes_filtrados, porcentaje_acumulado)

def filtrar_por_encima_votos(votos: list, limite_votos: int) -> tuple:
    total_votos = calcular_total_votos(votos)
    cantidad_cumplen = 0
    for i in range(len(votos)):
        if votos[i] > limite_votos:
            cantidad_cumplen += 1
    partidos_filtrados = [0] * cantidad_cumplen
    votos_filtrados = [0] * cantidad_cumplen
    porcentajes_filtrados = [0.0] * cantidad_cumplen
    indice = 0
    for i in range(len(votos)):
        if votos[i] > limite_votos:
            porcentaje = (votos[i] / total_votos) * 100
            partidos_filtrados[indice] = i + 1
            votos_filtrados[indice] = votos[i]
            porcentajes_filtrados[indice] = porcentaje
            indice += 1
            
    return (partidos_filtrados, votos_filtrados, porcentajes_filtrados)

def obtener_partidos_menos_votados(votos: list) -> tuple:
    total_votos = calcular_total_votos(votos)
    menor_voto = encontrar_menor_voto(votos)
    cantidad_minimos = 0
    for v in votos:
        if v == menor_voto:
            cantidad_minimos += 1
    partidos_filtrados = [0] * cantidad_minimos
    votos_filtrados = [0] * cantidad_minimos
    porcentajes_filtrados = [0.0] * cantidad_minimos
    indice = 0
    for i in range(len(votos)):
        if votos[i] == menor_voto:
            partidos_filtrados[indice] = i + 1
            votos_filtrados[indice] = votos[i]
            porcentajes_filtrados[indice] = (votos[i] / total_votos) * 100
            indice += 1         
    return (partidos_filtrados, votos_filtrados, porcentajes_filtrados)

def evaluar_segunda_vuelta_logica(votos: list) -> list:
    total_votos = calcular_total_votos(votos)
    mayor_voto = encontrar_mayor_voto(votos) 
    ganador_id = 0
    for i in range(len(votos)):
        if votos[i] == mayor_voto:
            ganador_id = i + 1
            break      
    porcentaje_ganador = (mayor_voto / total_votos) * 100
    if porcentaje_ganador <= 50.0:
        return [True, ganador_id, mayor_voto, porcentaje_ganador]
    else:
        return [False, ganador_id, mayor_voto, porcentaje_ganador]

def ordenar_nombres_alfabeticamente(lista_nombres: list) -> list:
    nombres_ordenados = [0] * len(lista_nombres)
    for i in range(len(lista_nombres)):
        nombres_ordenados[i] = lista_nombres[i]   
    limite = len(nombres_ordenados)
    for i in range(limite - 1):
        for j in range(0, limite - i - 1):
            if nombres_ordenados[j] > nombres_ordenados[j + 1]:
                auxiliar = nombres_ordenados[j]
                nombres_ordenados[j] = nombres_ordenados[j + 1]
                nombres_ordenados[j + 1] = auxiliar
                
    return nombres_ordenados
