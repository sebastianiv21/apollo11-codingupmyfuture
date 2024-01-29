import argparse
import logging
from app.utilities.validar_numeros import es_numero_positivo

LEVEL_CHOICES = [
    logging.NOTSET,
    logging.DEBUG,
    logging.INFO,
    logging.WARNING,
    logging.ERROR,
]


def get_app_args(logging_level: int) -> argparse.Namespace:
    try:
        # crear el objeto ArgumentParser
        parser = argparse.ArgumentParser(
            description="Apollo 11 - Módulo de configuración de argumentos"
        )

        # agregar argumentos
        parser.add_argument(
            "-p",
            "--periodicidad",
            type=es_numero_positivo,
            help="Periodicidad de ejecución en segundos por ciclo.",
            dest="periodicidad",
        )

        parser.add_argument(
            "-l",
            "--level",
            type=int,
            help="Nivel de detalle logging.",
            default=logging_level,
            choices=LEVEL_CHOICES,
            dest="logging_level",
        )

        # analizar los argumentos
        args = parser.parse_args()

        return args
    except Exception as e:
        raise Exception(f"Error al obtener los argumentos del programa: {e}")


# print(f"nivel de detalle: {args.logging_level}")
