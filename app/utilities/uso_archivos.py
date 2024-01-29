import logging
import os
import shutil


def mover_contenido_carpeta(
    carpeta_origen: str, carpeta_destino: str, logger: logging.Logger
) -> None:
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

    except FileNotFoundError:
        # Manejar el caso en que el archivo no se encuentre
        raise FileNotFoundError(f"No se encontraron archivos en '{carpeta_origen}'")

    except NotADirectoryError:
        # Manejar el caso en que la carpeta de destino no sea un directorio válido
        raise NotADirectoryError(
            f"La carpeta de destino '{carpeta_destino}' no es un directorio válido."
        )

    except shutil.Error as e:
        # Manejar errores relacionados con la operación de movimiento
        raise shutil.Error(f"Error al mover el contenido: {e}")

    except Exception as e:
        raise Exception(f"Ocurrió un error al mover el contenido: {e}")
