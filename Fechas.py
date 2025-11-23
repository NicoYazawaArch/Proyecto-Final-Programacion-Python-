#/Fechas.py

def es_bisiesto(año):
    """
    Valida si un año es bisiesto.
    Recibe: año (int).
    Retorna: True o False.
    """
    # Un año es bisiesto si es (divisible por 4 Y NO por 100) O (es divisible por 400).
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def dias_en_mes(mes, año):
    """
    Calcula la cantidad de días de un mes/año.
    Recibe: mes (int), año (int).
    Retorna: El número de días (int). Retorna 0 si el mes es inválido.
    """
    
    MESES_30_DIAS = (4, 6, 9, 11)
    MESES_31_DIAS = (1, 3, 5, 7, 8, 10, 12)

    es_mes_30 = mes in MESES_30_DIAS
    es_mes_31 = mes in MESES_31_DIAS  
    es_bisiesto_val = es_bisiesto(año)

    if mes == 2 and es_bisiesto_val:
        dias = 29
    elif mes == 2:
        dias = 28
    elif es_mes_30:
        dias = 30
    elif es_mes_31:
        dias = 31
    else:  
        dias = 0
        
    return dias