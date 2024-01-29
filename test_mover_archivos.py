import os
import pytest
from src.mover_contenido import mover_contenido

# Define la ruta de las carpetas para las pruebas
CARPETA_ORIGEN = 'ruta_de_tu_carpeta_origen'
CARPETA_DESTINO = 'ruta_de_tu_carpeta_destino'


@pytest.fixture
def setup_test_folders():
    # Crea carpetas de prueba y agrega archivos de prueba
    os.makedirs(CARPETA_ORIGEN, exist_ok=True)
    os.makedirs(CARPETA_DESTINO, exist_ok=True)
    with open(os.path.join(CARPETA_ORIGEN, 'archivo1.txt'), 'w') as f:
        f.write('Contenido de prueba')


def test_mover_contenido(setup_test_folders):
    # Llama a la función y verifica el resultado
    mover_contenido(CARPETA_ORIGEN, CARPETA_DESTINO)

    # Verifica que los archivos se hayan movido correctamente
    assert not os.path.exists(os.path.join(CARPETA_ORIGEN, 'archivo1.txt'))
    assert os.path.exists(os.path.join(CARPETA_DESTINO, 'archivo1.txt'))
