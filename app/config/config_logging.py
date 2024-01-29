import logging


def get_logger(
    formato_fecha_log: str, formato_contenido_log: str, nivel_logging: int
) -> logging.Logger:
    """
    Genera un objeto Logger configurado para registrar eventos

    Args:
        formato_fecha_log (str): formato de la fecha en los logs
        formato_contenido_log (str): formato del contenido en los logs
        nivel_logging (int): nivel de logging

    Returns:
        logging.Logger: objeto Logger configurado para registrar eventos
    """
    try:
        # Configuración global del registro
        logging.basicConfig(
            level=nivel_logging, format=formato_contenido_log, datefmt=formato_fecha_log
        )

        # Obtén el objeto Logger configurado
        logger: logging.Logger = logging.getLogger(__name__)

        return logger
    except Exception as e:
        raise Exception(f"Error al obtener el logger: {e}")
