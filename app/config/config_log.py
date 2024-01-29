import logging

formato = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"

# Configuración global del registro
logging.basicConfig(level=logging.INFO, format=formato, datefmt="%d-%m-%Y %H:%M:%S")

# Obtén el objeto Logger configurado
logger = logging.getLogger(__name__)
