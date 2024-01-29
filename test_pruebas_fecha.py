from typing import Optional
from datetime import datetime


def formatear_fecha(fecha: datetime, con_hora: Optional[bool] = True) -> str:
    formato = "%d/%m/%Y %H:%M:%S" if con_hora else "%d/%m/%Y"
    return fecha.strftime(formato)

# Tests utilizando pytest


def test_formatear_fecha_con_hora():
    fecha = datetime(2023, 12, 17, 15, 30, 45)
    resultado = formatear_fecha(fecha)
    assert resultado == "17/12/2023 15:30:45"


def test_formatear_fecha_sin_hora():
    fecha = datetime(2023, 12, 17, 15, 30, 45)
    resultado = formatear_fecha(fecha, con_hora=False)
    assert resultado == "17/12/2023"


def test_formatear_fecha_default():
    fecha = datetime(2023, 12, 17, 15, 30, 45)
    resultado = formatear_fecha(fecha)
    assert resultado == "17/12/2023 15:30:45"


# Ejecutar los tests con pytest
# Guarda este script en un archivo con extensión ->
# .py, por ejemplo, test_fecha.py
# Luego ejecuta pytest en la terminal en el mismo ->
# directorio donde se encuentra el archivo.
