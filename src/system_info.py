"""Obtiene información real del computador y la guarda en data/system_info.json."""

import json
import platform
from pathlib import Path

import numpy as np
import psutil


def obtener_valor(funcion):
    """Ejecuta una función y devuelve su resultado o 'No disponible'."""
    try:
        return funcion()
    except (AttributeError, NotImplementedError):
        return "No disponible"


def obtener_info_sistema():
    """Recopila la información básica del sistema en un diccionario."""
    return {
        "sistema_operativo": obtener_valor(lambda: platform.system()),
        "arquitectura": obtener_valor(lambda: platform.machine()),
        "version_python": obtener_valor(lambda: platform.python_version()),
        "version_numpy": obtener_valor(lambda: np.__version__),
        "procesador": obtener_valor(lambda: platform.processor()),
        "nucleos_fisicos": obtener_valor(lambda: psutil.cpu_count(logical=False)),
        "procesadores_logicos": obtener_valor(lambda: psutil.cpu_count(logical=True)),
        "memoria_ram_total_bytes": obtener_valor(
            lambda: psutil.virtual_memory().total
        ),
    }


def guardar_info_sistema(info, ruta):
    """Guarda la información en formato JSON legible, creando la carpeta."""
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(info, archivo, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    info = obtener_info_sistema()
    ruta_salida = Path(__file__).resolve().parent.parent / "data" / "system_info.json"
    guardar_info_sistema(info, ruta_salida)
    print(json.dumps(info, ensure_ascii=False, indent=4))
