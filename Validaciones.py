#/Validaciones.py

from Fechas import dias_en_mes

def es_año_valido(año):
    """
    Propósito: Valida si el año está en el rango [2024-2034].
    Recibe: año (int).
    Retorna: True o False.
    """
    es_mayor_igual = año >= 2024
    es_menor_igual = año <= 2034
    return es_mayor_igual and es_menor_igual

def es_mes_valido(mes):
    """
    Propósito: Valida si el mes de período es 3, 6, 9 o 12.
    Recibe: mes (int).
    Retorna: True o False.
    """
    return mes in (3, 6, 9, 12)

def es_fecha_valida(dia_ing, mes_ing, año_ing, año_periodo, mes_periodo):
    """
    Propósito: Valida si la fecha existe Y si pertenece al período estacional.
    Recibe: dia_ing, mes_ing, año_ing, año_periodo, mes_periodo (int).
    Retorna: True o False.
    """
    
    # Validar existencia en calendario
    # Se llama a la función importada
    max_dias_mes = dias_en_mes(mes_ing, año_ing)
    existe_fecha = (año_ing > 0 and 1 <= mes_ing <= 12 and 1 <= dia_ing <= max_dias_mes)

    # Validar pertenencia al período
    es_periodo_3 = (mes_periodo == 3 and año_ing == año_periodo and (mes_ing in (3, 4, 5)))
    es_periodo_6 = (mes_periodo == 6 and año_ing == año_periodo and (mes_ing in (6, 7, 8)))
    es_periodo_9 = (mes_periodo == 9 and año_ing == año_periodo and (mes_ing in (9, 10, 11)))
    
    es_periodo_12_p1 = (mes_periodo == 12 and año_ing == año_periodo and mes_ing == 12)
    es_periodo_12_p2 = (mes_periodo == 12 and año_ing == (año_periodo + 1) and (mes_ing in (1, 2)))
    es_periodo_12 = (es_periodo_12_p1 or es_periodo_12_p2)
    
    en_periodo_valido = (es_periodo_3 or es_periodo_6 or es_periodo_9 or es_periodo_12)

    return (existe_fecha and en_periodo_valido)

def es_habitacion_valida(nro_hab, tupla_s, tupla_d, tupla_t):
    """
    Propósito: Valida si el número de habitación existe.
    Recibe: nro_hab (int), tupla_s, tupla_d, tupla_t (tuples).
    Retorna: True o False.
    """
    es_simple = nro_hab in tupla_s
    es_doble = nro_hab in tupla_d
    es_triple = nro_hab in tupla_t
    return es_simple or es_doble or es_triple

def es_dias_valido(cant_dias):
    """
    Propósito: Valida si la cantidad de días está en el rango (0, 93).
    Recibe: cant_dias (int).
    Retorna: True o False.
    """
    es_mayor_cero = cant_dias > 0
    es_menor_93 = cant_dias < 93
    
    return es_mayor_cero and es_menor_93