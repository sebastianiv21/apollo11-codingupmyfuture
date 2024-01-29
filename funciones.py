import random
import os
import yaml
from datetime import datetime
from typing import List, Dict

from se_supone import generar_reportes


def generar_nombre_archivo(mission_code: str, num: int) -> str:
    """
    Genera el nombre de un archivo basado en el código de misión y un número.

    Parameters:
    - mission_code (str): Código de la misión.
    - num (int): Número del archivo.

    Returns:
    str: Nombre del archivo generado.
    """
    try:
        return f"APL{mission_code}-{num:04d}.log"
    except Exception as e:
        print(f"Error al generar el nombre del archivo: {e}")
        raise


def generar_estado_dispositivo() -> str:
    """
    Genera un estado aleatorio para un dispositivo.

    Returns:
    str: Estado aleatorio del dispositivo.
    """
    try:
        estados = ['excellent', 'good', 'warning',
                   'faulty', 'killed', 'unknown']
        return random.choice(estados)
    except Exception as e:
        print(f"Error al generar el estado del dispositivo: {e}")
        raise


def obtener_nombre_mision(mission_code: str) -> str:
    """
    Obtiene el nombre de la misión basado en el código.

    Parameters:
    - mission_code (str): Código de la misión.

    Returns:
    str: Nombre de la misión.
    """
    try:
        misiones = {'ORBONE': 'OrbitOne', 'CLNM': 'ColonyMoon',
                    'TMRS': 'VacMars', 'GALXONE': 'GalaxyTwo', 'UNKN': 'Unknown'}
        return misiones.get(mission_code, 'Unknown')
    except Exception as e:
        print(f"Error al obtener el nombre de la misión: {e}")
        raise


def generar_tipo_dispositivo() -> str:
    """
    Genera un tipo aleatorio de dispositivo.

    Returns:
    str: Tipo aleatorio de dispositivo.
    """
    try:
        tipos_dispositivos = ['Satelites', 'Naves',
                              'Trajes', 'Vehiculos espaciales']
        return random.choice(tipos_dispositivos)
    except Exception as e:
        print(f"Error al generar el tipo de dispositivo: {e}")
        raise


def generar_contenido_archivo(mission_code: str, num: int) -> str:
    """
    Genera el contenido de un archivo YAML con datos aleatorios.

    Parameters:
    - mission_code (str): Código de la misión.
    - num (int): Número del archivo.

    Returns:
    str: Contenido del archivo en formato YAML.
    """
    try:
        fecha_actual = datetime.now().strftime('%d%m%Y%H%M%S')

        if mission_code == 'UNKN':
            data = {'date': fecha_actual, 'mission': obtener_nombre_mision(mission_code),
                    'device_type': generar_tipo_dispositivo(), 'device_status': 'unknown', 'hash': 'unknown'}
        else:
            device_type = f"Device_{num}"
            device_status = generar_estado_dispositivo()
            hash_value = hash(
                f"{mission_code}{fecha_actual}{device_type}{device_status}")

            data = {'date': fecha_actual, 'mission': obtener_nombre_mision(mission_code),
                    'device_type': generar_tipo_dispositivo(), 'device_status': device_status, 'hash': hash_value}

        return yaml.dump(data, default_flow_style=False)
    except Exception as e:
        print(f"Error al generar el contenido del archivo: {e}")
        raise


def generar_archivos_mision(num_archivos: int, directorio: str) -> None:
    """
    Genera archivos de misiones con datos aleatorios y los guarda en un directorio.

    Parameters:
    - num_archivos (int): Número de archivos a generar.
    - directorio (str): Directorio donde se guardarán los archivos.
    """
    try:
        # Crear el directorio si no existe
        if not os.path.exists(directorio):
            os.makedirs(directorio)

        for i in range(1, num_archivos + 1):
            mission_code = random.choice(
                ['ORBONE', 'CLNM', 'TMRS', 'GALXONE', 'UNKN'])
            nombre_archivo = generar_nombre_archivo(mission_code, i)
            ruta_completa = os.path.join(directorio, nombre_archivo)
            contenido_archivo = generar_contenido_archivo(mission_code, i)

            with open(ruta_completa, 'w') as file:
                file.write(contenido_archivo)
    except Exception as e:
        print(f"Error al generar archivos de misiones: {e}")
        raise


if __name__ == "__main__":
    """
    Punto de entrada principal del script.
    """
    try:
        num_archivos = random.randint(50, 50)
        generar_archivos_mision(num_archivos, 'uuid')
        generar_reportes('uuid', 'devices')
    except Exception as e:
        print(f"Error en la ejecución del programa: {e}")
