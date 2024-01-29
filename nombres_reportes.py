import datetime


def generar_nombre_archivo(reporte):
    """
    Genera un nombre de archivo siguiendo el estándar APLSTATS-[REPORTE]-ddmmyyHHMISS.log.

    Parámetros:
    - reporte (str): El nombre del reporte para incluir en el nombre del archivo.

    Retorna:
    - str: El nombre de archivo generado.

    Ejemplo de uso:
    >>> generar_nombre_archivo("REPORTE1")
    'APLSTATS-REPORTE1-260124152345.log'
    """
    try:
        # Obtener la fecha y hora actual
        fecha_hora_actual = datetime.datetime.now()

        # Formatear la fecha y hora según el estándar especificado
        formato_fecha_hora = fecha_hora_actual.strftime("%d%m%y%H%M%S")

        # Construir el nombre del archivo
        nombre_archivo = f"APLSTATS-{reporte}-{formato_fecha_hora}.log"

        return nombre_archivo

    except Exception as e:
        # Manejar cualquier excepción y mostrar un mensaje de error
        return f"Error al generar el nombre del archivo: {str(e)}"


# Ejemplo de uso
try:
    nombre_archivo_generado = generar_nombre_archivo("REPORTE1")
    print(nombre_archivo_generado)
except Exception as e:
    print(f"Error: {str(e)}")
