import shutil
import os
from config_log import logger
from typing import Union


def mover_contenido(origen: str, destino: str) -> None:
    """
    Mueve todo el contenido de una carpeta de origen a una carpeta de destino.

    Parámetros:
    - origen (str): La ruta de la carpeta de origen.
    - destino (str): La ruta de la carpeta de destino.

    Excepciones:
    - FileNotFoundError: Se levanta si no se encuentran
        archivos en la carpeta de origen.
    - NotADirectoryError: Se levanta si la carpeta de
        destino no es un directorio válido.
    - shutil.Error: Se levanta si hay errores relacionados
        con la operación de movimiento.
    - Exception: Se levanta para manejar
        cualquier otra excepción no prevista.
    """
    try:
        # Si la carpeta destino no existe, la crea
        if not os.path.exists(destino):
            os.makedirs(destino)

        # Mover el contenido de la carpeta de origen a la carpeta destino
        for elemento in os.listdir(origen):
            origen_path = os.path.join(origen, elemento)
            destino_path = os.path.join(destino, elemento)
            shutil.move(origen_path, destino_path)

        # Registrar mensaje de movimiento exitoso
        logger.info(f"Contenido de {origen} se movió a {destino}")

    except FileNotFoundError:
        # Manejar el caso en que el archivo no se encuentre
        logger.error(
            f"No se encontraron archivos en la carpeta {origen}.")

    except NotADirectoryError:
        # Manejar el caso en que la carpeta de destino
        # no sea un directorio válido
        logger.error(
            f"La ruta de destino {destino} no es válida.")

    except shutil.Error as e:
        # Manejar errores relacionados con la operación de movimiento
        logger.error(f"No se movió el contenido de {origen} Error:{e}")

    except Exception as e:
        # Manejar cualquier otra excepción no prevista
        logger.error(f"Ocurrió un error inesperado: {e}")


# Ejemplo de uso
origen = '../apollo11/mover'
destino = '../apollo11/devices'

mover_contenido(origen, destino)
