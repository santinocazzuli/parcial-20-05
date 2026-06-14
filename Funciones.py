def calcular_total_votos(votos_partidos: list) -> int:
    total = 0
    for voto in votos_partidos:
        total += voto
    return total

def calcular_promedio_votos(votos_partidos: list) -> float:
    total_votos = calcular_total_votos(votos_partidos)
    cantidad_partidos = len(votos_partidos)
    if cantidad_partidos == 0:
        return 0.0
    return total_votos / cantidad_partidos

def encontrar_menor_voto(votos_partidos: list) -> int:
    menor = votos_partidos[0]
    for voto in votos_partidos:
        if voto < menor:
            menor = voto
    return menor

def encontrar_mayor_voto(votos_partidos: list) -> int:
    mayor = votos_partidos[0]
    for voto in votos_partidos:
        if voto > mayor:
            mayor = voto
    return mayor

def filtrar_por_debajo_porcentaje(votos_partidos: list, limite_porcentaje: float) -> list:
    total_votos = calcular_total_votos(votos_partidos)
    partidos_filtrados = []
    votos_filtrados = []
    porcentajes_filtrados = []
    porcentaje_acumulado = 0.0
    for i in range(len(votos_partidos)):
        porcentaje = (votos_partidos[i] / total_votos) * 100
        if porcentaje < limite_porcentaje:
            partidos_filtrados.append(i + 1)
            votos_filtrados.append(votos_partidos[i])
            porcentajes_filtrados.append(porcentaje)
            porcentaje_acumulado += porcentaje
    return [partidos_filtrados, votos_filtrados, porcentajes_filtrados, porcentaje_acumulado]

def filtrar_por_encima_votos(votos_partidos: list, minimo_votos: int) -> list:
    total_votos = calcular_total_votos(votos_partidos)
    partidos_filtrados = []
    votos_filtrados = []
    porcentajes_filtrados = []
    for i in range(len(votos_partidos)):
        if votos_partidos[i] > minimo_votos:
            partidos_filtrados.append(i + 1)
            votos_filtrados.append(votos_partidos[i])
            porcentajes_filtrados.append((votos_partidos[i] / total_votos) * 100)
    return [partidos_filtrados, votos_filtrados, porcentajes_filtrados]

def obtener_partidos_menos_votados(votos_partidos: list) -> list:
    menor_voto = encontrar_menor_voto(votos_partidos)
    total_votos = calcular_total_votos(votos_partidos)
    partidos_indices = []
    partidos_votos = []
    partidos_porcentajes = []
    for i in range(len(votos_partidos)):
        if votos_partidos[i] == menor_voto:
            partidos_indices.append(i + 1)
            partidos_votos.append(votos_partidos[i])
            partidos_porcentajes.append((votos_partidos[i] / total_votos) * 100)
    return [partidos_indices, partidos_votos, partidos_porcentajes]

def evaluar_segunda_vuelta_logica(votos_partidos: list) -> list:
    total_votos = calcular_total_votos(votos_partidos)
    mayor_voto = encontrar_mayor_voto(votos_partidos)
    id_ganador = -1
    for i in range(len(votos_partidos)):
        if votos_partidos[i] == mayor_voto:
            id_ganador = i + 1
            break
    porcentaje_ganador = (mayor_voto / total_votos) * 100
    if porcentaje_ganador <= 50.0:
        return [True, id_ganador, mayor_voto, porcentaje_ganador]
    return [False, id_ganador, mayor_voto, porcentaje_ganador]

def ordenar_nombres_alfabeticamente(lista_nombres: list) -> list:
    nombres_ordenados = []
    for nombre in lista_nombres:
        nombres_ordenados.append(nombre)
    limite = len(nombres_ordenados)
    for i in range(limite - 1):
        for j in range(0, limite - i - 1):
            if nombres_ordenados[j] > nombres_ordenados[j + 1]:
                auxiliar = nombres_ordenados[j]
                nombres_ordenados[j] = nombres_ordenados[j + 1]
                nombres_ordenados[j + 1] = auxiliar
    return nombres_ordenados
