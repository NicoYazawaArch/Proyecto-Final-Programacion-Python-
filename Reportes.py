#/Reportes.py

def mostrar_detalle_estadia(dni, nombre, apellido, fecha, tipo_hab, cant_dias):
    """
    Propósito: Imprime en pantalla el detalle de una estadía válida.
    Recibe: Todos los datos de la estadía.
    Retorna: Nada (solo imprime).
    """
    print("--- Detalle de Estadía Válida ---")
    print(f"DNI: {dni}")
    print(f"Huésped: {nombre} {apellido}")

    print(f"Fecha Ingreso: {fecha[0]}/{fecha[1]}/{fecha[2]}")
    print(f"Tipo Habitación: {tipo_hab}")
    print(f"Días Estadía: {cant_dias}")
    print("---------------------------------")

def mostrar_reporte_final(total_estadias, dias_s, dias_d, dias_t, cant_hab_s, cant_hab_d, cant_hab_t):
    """
    Propósito: Imprime en pantalla el reporte estadístico final.
    Recibe: Todos los contadores finales y las cantidades de habitaciones.
    Retorna: Nada (solo imprime).
    """
    
    print("--- REPORTE ESTADÍSTICO FINAL ---")
    print(f"Cantidad total de estadías del período: {total_estadias}")

    # Nivel de Uso Simple
    nivel_uso_s = 0 
    if cant_hab_s > 0:
        nivel_uso_s = dias_s / cant_hab_s
    print("--- Tipo Simple ---")
    print(f"Cantidad de días de ocupación: {dias_s}")
    print(f"Nivel de uso: {nivel_uso_s}")

    # Nivel de Uso Doble
    nivel_uso_d = 0
    if cant_hab_d > 0:
        nivel_uso_d = dias_d / cant_hab_d
    print("--- Tipo Doble ---")
    print(f"Cantidad de días de ocupación: {dias_d}")
    print(f"Nivel de uso: {nivel_uso_d}")

    # Nivel de Uso Triple
    nivel_uso_t = 0
    if cant_hab_t > 0:
        nivel_uso_t = dias_t / cant_hab_t
    print("--- Tipo Triple ---")
    print(f"Cantidad de días de ocupación: {dias_t}")
    print(f"Nivel de uso: {nivel_uso_t}")