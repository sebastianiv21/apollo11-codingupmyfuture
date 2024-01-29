import logging
formato = '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'
# Configuración global del registro
logging.basicConfig(filename='registro_global.log', level=logging.INFO,
                    format=formato)


# Obtén el objeto Logger configurado
logger = logging.getLogger(__name__)
