import yaml
from yaml.loader import SafeLoader
from typing import Optional, Dict, Any


def leer_yaml(path: str) -> Optional[Dict[str, Any]]:
    """
    Lee un archivo YAML y devuelve su contenido como un diccionario o None si hay un error.

    Args:
        path (str): Ruta del archivo YAML.

    Returns:
        dict or None: Diccionario con los datos YAML, o None si hay un error.
    """
    content: Optional[Dict[str, Any]] = None
    try:
        with open(path, "r") as file:
            content = yaml.load(file, Loader=SafeLoader)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo YAML en la ruta: {path}")
    except yaml.YAMLError as yaml_error:
        raise yaml.YAMLError(f"Error de formato YAML en {path}: {yaml_error}")
    except Exception as e:
        raise Exception(f"Error desconocido al leer el archivo YAML en {path}: {e}")
    return content
