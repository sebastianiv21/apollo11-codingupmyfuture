# importan librerías
import argparse
import os
from typing import Any, Dict, Optional
from app.config.config_argparse import get_app_args
from app.main.apollo11 import Apollo11
from app.models.config_model import ConfigModel
from app.utilities.uso_yaml import leer_yaml

# Ruta del directorio del script
script_dir = os.path.dirname(__file__)

# Combina la ruta del directorio del script con la ruta relativa del archivo config_app.yaml
config_file_path = os.path.join(script_dir, "app", "config", "config_app.yaml")


class App:
    if __name__ == "__main__":
        try:
            # Configuración de parámetros
            plain_config: Optional[Dict[str, Any]] = leer_yaml(config_file_path)

            config: ConfigModel = ConfigModel(**plain_config)

            # obtiene valores de los argumentos
            args: argparse.Namespace = get_app_args(config.logging_level)
            print(args.periodicidad, args.logging_level)

            # actualiza los valores de la configuración por defecto
            if args.periodicidad:
                config.periodicidad = args.periodicidad

            if args.logging_level:
                config.logging_level = args.logging_level

            apollo11 = Apollo11(config)

            # ejecuta el programa
            apollo11.run()
            # if generador_archivos:
            # llamar función principal de una clase para generarlos (entrada)
            # pass
            # elif generar_reportes:
            # llamar función principal de una clase para generarlos (entrada)
            # pass
            # manejo de excepción
        except Exception as e:
            print(e)
