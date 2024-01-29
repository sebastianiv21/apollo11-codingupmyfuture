import os
import shutil
from ..config.config_log import logger


def mover_contenido_carpeta(carpeta_origen: str, carpeta_destino: str) -> None:
    """
    Mueve todo el contenido de una carpeta de origen a una carpeta de destino.

    Args:
        carpeta_origen (str): La ruta de la carpeta de origen.
        carpeta_destino (str): La ruta de la carpeta de destino.

    Excepctions:
        FileNotFoundError: Se levanta si no se encuentran archivos en la carpeta de origen.
        NotADirectoryError: Se levanta si la carpeta de destino no es un directorio válido.
        shutil.Error: Se levanta si hay errores relacionados con la operación de movimiento.
        Exception: Se levanta para manejar cualquier otra excepción no prevista.

    Returns:
        None. No hay un valor de retorno explícito.
    """
    try:
        # Verificar si la carpeta de origen existe
        if not os.path.exists(carpeta_origen):
            raise FileNotFoundError(
                f"La carpeta de origen '{carpeta_origen}' no existe."
            )

        # Si la carpeta destino no existe, la crea
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

        # Mover el contenido de la carpeta de origen a la carpeta destino
        for archivo in os.listdir(carpeta_origen):
            origen_path: str = os.path.join(carpeta_origen, archivo)
            destino_path: str = os.path.join(carpeta_destino, archivo)
            shutil.move(origen_path, destino_path)

        # Registrar mensaje de movimiento exitoso
        logger.info(f"Contenido de '{carpeta_origen}' se movió a '{carpeta_destino}'")

    except FileNotFoundError as e:
        # Manejar el caso en que el archivo no se encuentre
        logger.error(str(e))

    except NotADirectoryError as e:
        # Manejar el caso en que la carpeta de destino no sea un directorio válido
        logger.error(str(e))

    except shutil.Error as e:
        # Manejar errores relacionados con la operación de movimiento
        logger.error(f"No se movió el contenido de '{carpeta_origen}' Error: {e}")

    except Exception as e:
        # Manejar cualquier otra excepción no prevista
        logger.error(f"Ocurrió un error inesperado: {e}")
