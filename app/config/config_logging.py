import logging

# formato de la fecha en los logs
formato_fecha_log: str = "%d-%m-%Y %H:%M:%S"


# formato del contenido en los logs
formato_contenido_log: str = "%(asctime)s\t%(levelname)s\t%(message)s"

nivel_logging: int = logging.DEBUG


def get_logger(
    formato_fecha_log: str, formato_contenido_log: str, nivel_logging: int
) -> logging.Logger:
    # Configuración global del registro
    logging.basicConfig(
        level=nivel_logging, format=formato_contenido_log, datefmt=formato_fecha_log
    )

    # Obtén el objeto Logger configurado
    logger: logging.Logger = logging.getLogger(__name__)

    return logger
