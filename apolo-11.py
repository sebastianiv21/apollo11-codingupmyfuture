# importan librerías
import time
import argparse
import logging
import os
from typing import Any, Dict, Optional
from app.archivos.funciones import generar_archivos_mision
from app.config.config_argparse import get_app_args
from app.config.config_logging import get_logger
from app.main.apollo11 import Apollo11
from app.models.config_model import ConfigModel
from app.utilities.uso_yaml import leer_yaml

# Ruta del directorio del script
script_dir = os.path.dirname(__file__)

# Combina la ruta del directorio del script con la ruta relativa del archivo config_app.yaml
config_file_path = os.path.join(script_dir, "app", "config", "config_app.yaml")

directiorio_archivos_mision = os.path.join(script_dir, "devices")


# # Ejemplo de uso del decorador
# @periodic_task(interval=2)  # Cambia el intervalo según tus necesidades
# def generador_archivos():
#     # Lógica de generación de archivos
#     print("Generando archivos...")


class App:
    if __name__ == "__main__":
        try:
            # Configuración de parámetros
            plain_config: Optional[Dict[str, Any]] = leer_yaml(config_file_path)

            config: ConfigModel = ConfigModel(**plain_config)

            # obtiene valores de los argumentos
            args: argparse.Namespace = get_app_args(config.logging_level)

            # actualiza los valores de la configuración por defecto
            if args.periodicidad:
                config.periodicidad = args.periodicidad

            if args.logging_level:
                config.logging_level = args.logging_level

            # obtiene el logger
            logger: logging.Logger = get_logger(
                formato_fecha_log=config.formato_fecha_log,
                formato_contenido_log=config.formato_contenido_log,
                nivel_logging=config.logging_level,
            )

            logger.info("Iniciando programa")
            apollo11 = Apollo11(config)

            # ejecuta el programa
            apollo11.run()

            # Ejecuta generador_archivos periódicamente
            while True:
                generar_archivos_mision(
                    num_archivos=config.cantidad_archivos_generados,
                    misiones=config.misiones.keys(),
                    directorio=directiorio_archivos_mision,
                )
                time.sleep(config.periodicidad)

        except Exception as e:
            logger.error(e)
