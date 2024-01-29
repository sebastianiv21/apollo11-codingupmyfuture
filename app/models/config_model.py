from typing import Dict, List
from pydantic import BaseModel


class Archivo(BaseModel):
    cantidad_minima: int
    cantidad_maxima: int
    formato_fecha: str


class Config(BaseModel):
    ciclo_simulacion: int
    logging_level: int
    archivos: Archivo
    misiones: List[Dict[str, str]]
    dispositivos: List[str]
    estados_dispositivo: List[str]
