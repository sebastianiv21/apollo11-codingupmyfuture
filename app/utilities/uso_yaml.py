import yaml
from yaml.loader import SafeLoader
from typing import Optional, Dict
from ..config.config_log import logger


def leer_yaml(path: str) -> Optional[Dict]:
    """
    Lee un archivo YAML y devuelve su contenido como un diccionario o None si hay un error.

    Args:
        path (str): Ruta del archivo YAML.

    Returns:
        dict or None: Diccionario con los datos YAML, o None si hay un error.
    """
    content: Optional[Dict] = None
    try:
        with open(path) as file:
            content = yaml.load(file, Loader=SafeLoader)
    except FileNotFoundError:
        logger.error(f"No se encontró el archivo YAML en la ruta: {path}")
    except yaml.YAMLError as yaml_error:
        logger.error(f"Error de formato YAML en {path}: {yaml_error}")
    except Exception as e:
        logger.error(f"Error desconocido al leer el archivo YAML en {path}: {e}")
    return content
