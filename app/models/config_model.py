from typing import Dict, List
from pydantic import BaseModel


class CantidadArchivosModel(BaseModel):
    minimo: int
    maximo: int


class ConfigModel(BaseModel):
    periodicidad: int
    logging_level: int
    cantidad_archivos_generados: CantidadArchivosModel
    formato_fecha_archivo: str
    formato_fecha_log: str
    formato_contenido_log: str
    misiones: Dict[str, str]
    dispositivos: List[str]
    estados_dispositivo: List[str]
