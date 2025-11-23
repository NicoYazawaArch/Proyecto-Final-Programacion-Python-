#/Procesamiento.py

def determinar_tipo_habitacion(nro_hab, tupla_s, tupla_d, tupla_t):
    """
    Propósito: Retorna el tipo de habitación como una cadena.
    Recibe: nro_hab (int), tupla_s, tupla_d, tupla_t (tupla).
    Retorna: "Simple", "Doble" o "Triple" (str).
    """
    # Se asume que nro_hab ya fue validado por es_habitacion_valida
    
    if nro_hab in tupla_s:
        tipo = "Simple"
    elif nro_hab in tupla_d:
        tipo = "Doble"
    else: # Si no es Simple ni Doble, es Triple
        tipo = "Triple"
    return tipo

def actualizar_estadisticas(tipo_hab, cant_dias, cont_estadias, cont_dias_s, cont_dias_d, cont_dias_t):
    """
    Propósito: Acumula los contadores y los retorna.
    Recibe: tipo_hab (str), cant_dias (int), y todos los contadores actuales.
    Retorna: Una lista con los nuevos valores de los contadores.
    """
    # Asignamos los valores actuales como base
    nuevo_cont_estadias = cont_estadias + 1
    nuevo_cont_dias_s = cont_dias_s
    nuevo_cont_dias_d = cont_dias_d
    nuevo_cont_dias_t = cont_dias_t

    # Actualizamos el contador específico según el tipo
    if tipo_hab == "Simple":
        nuevo_cont_dias_s = cont_dias_s + cant_dias
    elif tipo_hab == "Doble":
        nuevo_cont_dias_d = cont_dias_d + cant_dias
    else: # Si no es Simple ni Doble, es Triple
        nuevo_cont_dias_t = cont_dias_t + cant_dias
        
    return [nuevo_cont_estadias, nuevo_cont_dias_s, nuevo_cont_dias_d, nuevo_cont_dias_t]