from datetime import datetime
from ..config.config_log import logger


def generar_nombre_archivo(reporte: str) -> str:
    """
    Genera un nombre de archivo siguiendo el estándar APLSTATS-[REPORTE]-ddmmyyHHMISS.log.

    Args:
    - reporte (str): El nombre del reporte para incluir en el nombre del archivo.

    Returns:
    - str: El nombre de archivo generado.
    """
    try:
        # Obtener la fecha y hora actual
        fecha_hora_actual = datetime.now()

        # Formatear la fecha y hora según el estándar especificado
        formato_fecha_hora = fecha_hora_actual.strftime("%d%m%y%H%M%S")

        # Construir el nombre del archivo
        nombre_archivo = f"APLSTATS-{reporte}-{formato_fecha_hora}.log"

        return nombre_archivo

    except Exception as e:
        # Manejar cualquier excepción y mostrar un mensaje de error en el logger
        logger.error(
            f"Error al generar el nombre del archivo para el reporte '{reporte}': {str(e)}"
        )
        return ""
