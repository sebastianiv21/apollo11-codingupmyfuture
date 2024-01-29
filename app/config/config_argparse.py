import argparse
import logging
from app.utilities.validar_numeros import es_numero_positivo

DEFAULT_LEVEL = logging.DEBUG
LEVEL_CHOICES = [
    logging.NOTSET,
    logging.DEBUG,
    logging.INFO,
    logging.WARNING,
    logging.ERROR,
]


# crear el objeto ArgumentParser
parser = argparse.ArgumentParser(
    description="Apollo 11 - Módulo de configuración de argumentos"
)

# agregar argumentos
# parser.add_argument("-f", "--file", help="Nombre del archivo", required=True)
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
    default=DEFAULT_LEVEL,
    choices=LEVEL_CHOICES,
    dest="logging_level",
)

# analizar los argumentos
args = parser.parse_args()

# mostrar valores
print(f"nivel de detalle: {args.logging_level}")
