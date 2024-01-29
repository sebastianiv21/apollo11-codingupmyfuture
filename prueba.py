import os
from typing import Optional
from src.config_log import logger


def crear_carpeta_devices(ruta: str, nombre: Optional[str] = 'devices') -> str:
    """
    Crea una carpeta llamada 'devices' en la ruta especificada.
    Parámetros:
    - ruta (str): La ruta en la que se creará la carpeta.
    - nombre (str, opcional): El nombre de la carpeta a crear.
        Por defecto, 'devices'.
    Retorna:
    - str: La ruta completa de la carpeta creada.
    """
    try:
        # Combinar la ruta y el nombre de la carpeta
        ruta_carpeta = os.path.join(ruta, nombre)

        # Verificar si la carpeta ya existe
        if os.path.exists(ruta_carpeta):
            raise FileExistsError(
                f"La carpeta '{ruta_carpeta}' ya ha sido creada")

        # Crear la carpeta
        os.makedirs(ruta_carpeta)

        # Verificar que la carpeta haya sido creada correctamente
        if not os.path.exists(ruta_carpeta):
            raise OSError(f"No se pudo crear la carpeta '{ruta_carpeta}'")

        return ruta_carpeta

    except (FileExistsError, OSError) as e:
        logger.error(f"Error al crear la carpeta: {e}.", exc_info=True)

    except Exception as e:
        logger.error(f'Error inesperado: {e}', exc_info=True)
        raise


crear_carpeta_devices('')
