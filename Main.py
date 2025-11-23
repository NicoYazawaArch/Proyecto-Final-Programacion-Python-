#//main2.py

# --- Importaciones ---
from Validaciones import (es_año_valido, es_mes_valido, es_fecha_valida, es_habitacion_valida, es_dias_valido)

from Procesamiento import (determinar_tipo_habitacion, actualizar_estadisticas)
from Reportes import (mostrar_detalle_estadia, mostrar_reporte_final)
from Entrada import (pedir_entero, pedir_cadena)

# --- Función Principal ---

def main():
    """
    Función principal que orquesta todo el programa.
    """
    HAB_SIMPLES = (201, 202)
    HAB_DOBLES = (101, 102, 103, 104, 105)
    HAB_TRIPLES = (31, 32, 33)
    
    CANT_HAB_S = len(HAB_SIMPLES)
    CANT_HAB_D = len(HAB_DOBLES)
    CANT_HAB_T = len(HAB_TRIPLES)

    # --- Inicialización de Contadores ---
    total_estadias = 0
    total_dias_simples = 0
    total_dias_dobles = 0
    total_dias_triples = 0

    # --- Ingreso del Período ---
    print("Sistema - La pulpería de Zoilo")

    # Validación para el AÑO
    año_valido = False
    año_periodo = 0
    while not año_valido:
        año_periodo = pedir_entero("Ingrese año del período (2024-2034): ")
        año_valido = es_año_valido(año_periodo)
        if not año_valido:
            print("Error. El año debe estar entre 2024 y 2034.")

    # Validación para el MES
    mes_valido = False
    mes_periodo = 0
    while not mes_valido:
        mes_periodo = pedir_entero("Ingrese mes de inicio del período (3, 6, 9, 12): ")
        mes_valido = es_mes_valido(mes_periodo)
        if not mes_valido:
            print("Error. El mes debe ser 3, 6, 9 o 12.")

    print(f"Período a analizar: {mes_periodo}/{año_periodo}")

    # --- Carga de Estadías ---
    seguir_cargando = True
    while seguir_cargando:
        
        respuesta = pedir_entero("¿Desea ingresar una nueva estadía? (1=Sí, 0=No): ")
        
        if respuesta == 1:
            # --- Ingreso y Validación ---
            dni = pedir_cadena("Ingrese DNI: ")
            nombre = pedir_cadena("Ingrese Nombre: ")
            apellido = pedir_cadena("Ingrese Apellido: ")
            
            # Validación para FECHA
            fecha_valida = False
            while not fecha_valida:
                dia_ing = pedir_entero("Ingrese DÍA de ingreso: ")
                mes_ing = pedir_entero("Ingrese MES de ingreso: ")
                año_ing = pedir_entero("Ingrese AÑO de ingreso: ")
                fecha_valida = es_fecha_valida(dia_ing, mes_ing, año_ing, año_periodo, mes_periodo)
                if not fecha_valida:
                    print("Error. Fecha no válida o fuera del período estacional seleccionado.")
            fecha_ing = [dia_ing, mes_ing, año_ing] 

            # Validación para HABITACIÓN
            hab_valida = False
            nro_hab = 0
            while not hab_valida:
                nro_hab = pedir_entero("Ingrese el número de habitación: ")
                hab_valida = es_habitacion_valida(nro_hab, HAB_SIMPLES, HAB_DOBLES, HAB_TRIPLES)
                if not hab_valida:
                    print("Error. Número de habitación no existente.")

            # Validación para DÍAS
            dias_validos = False
            cant_dias = 0
            while not dias_validos:
                cant_dias = pedir_entero("Ingrese la cantidad de días (1-92): ")
                dias_validos = es_dias_valido(cant_dias)
                if not dias_validos:
                    print("Error. Los días deben ser un número entre 1 y 92.")

            # --- Procesamiento ---
            
            tipo_hab = determinar_tipo_habitacion(nro_hab, HAB_SIMPLES, HAB_DOBLES, HAB_TRIPLES)
            
            mostrar_detalle_estadia(dni, nombre, apellido, fecha_ing, tipo_hab, cant_dias)
            
            # Actualizar contadores
            resultados_stats = actualizar_estadisticas(tipo_hab, cant_dias, total_estadias, total_dias_simples, total_dias_dobles, total_dias_triples)
            
            # Desempacar resultados de la lista
            total_estadias = resultados_stats[0]
            total_dias_simples = resultados_stats[1]
            total_dias_dobles = resultados_stats[2]
            total_dias_triples = resultados_stats[3]
            
        else: # Si la respuesta no fue 1
            seguir_cargando = False

    # --- Reporte Final ---
    print("... Fin de la carga de datos.")
    
    mostrar_reporte_final(total_estadias, total_dias_simples, total_dias_dobles, total_dias_triples, CANT_HAB_S, CANT_HAB_D, CANT_HAB_T)

main()